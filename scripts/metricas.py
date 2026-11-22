# Copia de scripts/metricas.py del kit agentes-con-control (MIT, del mismo autor).
# La usa la CI para calcular las cifras de la sección «Medido» de «Cómo se hace».
"""Métricas del trabajo de los agentes en un repositorio de GitHub.

Uso:
    python scripts/metricas.py --repo ORG/REPO [--dias 30] [--regla auto|etiqueta|rama|firma|todas]
                               [--etiqueta agente] [--prefijos claude/,agente/] [--incluir-bots]
                               [--costes costes.csv] [--salida metricas.json]

Lee los PR cerrados en la ventana de días y calcula, por separado para agentes y personas:

- PR fusionados y cerrados sin fusionar.
- Aceptados a la primera: de los PR con revisión formal en GitHub, los que nadie pidió cambiar.
- Commits después de abrir el PR (rondas de corrección), horas hasta la primera revisión y hasta fusionar.
- PR con pruebas y líneas de prueba.
- PR revertidos después (lo más parecido a la tasa de fallos de DORA que se ve desde GitHub).
- Coste por PR, si se da un CSV ``pr,usd``.

Los PR de bots (Dependabot, Renovate...) no cuentan, salvo con ``--incluir-bots``.

Token: ``GITHUB_TOKEN`` o ``GH_TOKEN`` del entorno o, si no hay, el de ``gh auth token``. Sin
token, GitHub deja 60 peticiones por hora. Solo usa la biblioteca estándar de Python.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shutil
import statistics
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path

API = "https://api.github.com"
PREFIJOS_POR_DEFECTO = ("claude/", "agente/", "copilot/", "codex/", "cursor/")
FIRMA_DE_AGENTE = re.compile(r"co-authored-by:.*\b(claude|copilot|codex|cursor|devin|aider)\b", re.IGNORECASE)
FICHERO_DE_PRUEBA = re.compile(
    r"(^|/)(tests?|__tests__|spec|specs)/|(^|/)src/test/|(^|/)test_[^/]+\.py$|_test\.(py|go)$|\.(test|spec)\.[cm]?[jt]sx?$|Tests?\.(java|kt)$",
    re.IGNORECASE,
)
REVERTIDO = re.compile(r"\bReverts\s+[\w.-]+/[\w.-]+#(\d+)|\brevert[s]?\s+#(\d+)", re.IGNORECASE)
NIVEL_SPEC = re.compile(r"(?im)^[^\w\n]*nivel de especificaci[oó]n[^\w\n]*:[^\w\n]*([0-3])\b")
COMENTARIO_HTML = re.compile(r"<!--.*?-->", re.DOTALL)
RUTAS_DE_ESPECIFICACION = ("openspec/", "especificaciones/")
REGLAS = ("auto", "etiqueta", "rama", "firma", "todas")


@dataclass
class PR:
    numero: int
    titulo: str
    autor: str
    rama: str
    etiquetas: list[str]
    creado: datetime
    cerrado: datetime | None
    fusionado: datetime | None
    cambios_pedidos: bool = False
    revisado: bool = False
    primera_revision: datetime | None = None
    lineas_prueba: int = 0
    lineas_totales: int = 0
    mensajes: list[str] = field(default_factory=list)
    commits_tras_abrir: int = 0
    es_bot: bool = False
    cuerpo: str = ""
    toca_especificacion: bool = False

    @property
    def nivel_spec(self) -> int | None:
        """Nivel del semáforo de especificación que declara la descripción del PR, si lo declara."""
        coincidencia = NIVEL_SPEC.search(COMENTARIO_HTML.sub("", self.cuerpo or ""))
        return int(coincidencia.group(1)) if coincidencia else None


def es_de_agente(pr: PR, regla: str = "auto", etiqueta: str = "agente", prefijos: tuple[str, ...] = PREFIJOS_POR_DEFECTO) -> bool:
    if regla == "todas":
        return True
    por_etiqueta = etiqueta.lower() in (e.lower() for e in pr.etiquetas)
    por_rama = pr.rama.lower().startswith(tuple(p.lower() for p in prefijos))
    por_firma = any(FIRMA_DE_AGENTE.search(m) for m in pr.mensajes)
    if regla == "etiqueta":
        return por_etiqueta
    if regla == "rama":
        return por_rama
    if regla == "firma":
        return por_firma
    if regla == "auto":
        return por_etiqueta or por_rama or por_firma
    raise ValueError(f"regla desconocida: {regla}")


def numeros_revertidos(prs: list[PR]) -> set[int]:
    """Números de PR que otro PR fusionado revirtió (el botón «Revert» de GitHub escribe «Reverts org/repo#N»)."""
    revertidos = set()
    for pr in prs:
        if pr.fusionado and pr.titulo.lower().startswith("revert"):
            for coincidencia in REVERTIDO.finditer(f"{pr.titulo}\n{pr.cuerpo}"):
                revertidos.add(int(coincidencia.group(1) or coincidencia.group(2)))
    return revertidos


def _porcentaje(parte: int, total: int) -> float | None:
    return round(100 * parte / total, 1) if total else None


def _mediana(valores: list[float]) -> float | None:
    return round(statistics.median(valores), 1) if valores else None


def _horas(desde: datetime, hasta: datetime) -> float:
    return (hasta - desde).total_seconds() / 3600


def _resumen(fusionados: list[PR], rechazados: list[PR], revertidos: set[int]) -> dict:
    n = len(fusionados)
    revisados = [p for p in fusionados if p.revisado]
    a_la_primera = sum(1 for p in revisados if not p.cambios_pedidos)
    con_pruebas = [p for p in fusionados if p.lineas_prueba > 0]
    revertidos_aqui = [p for p in fusionados if p.numero in revertidos]
    con_especificacion = [p for p in fusionados if p.toca_especificacion]
    niveles = [p.nivel_spec for p in fusionados if p.nivel_spec is not None]
    return {
        "con_especificacion": len(con_especificacion),
        "porcentaje_con_especificacion": _porcentaje(len(con_especificacion), n),
        "con_nivel_de_especificacion": len(niveles),
        "porcentaje_con_nivel_de_especificacion": _porcentaje(len(niveles), n),
        "niveles_de_especificacion": {str(k): niveles.count(k) for k in range(4) if niveles.count(k)},
        "fusionados": n,
        "cerrados_sin_fusionar": len(rechazados),
        "revisados": len(revisados),
        "aceptados_a_la_primera": a_la_primera,
        "porcentaje_a_la_primera": _porcentaje(a_la_primera, len(revisados)),
        "commits_tras_abrir_mediana": _mediana([float(p.commits_tras_abrir) for p in fusionados]),
        "horas_hasta_primera_revision_mediana": _mediana([_horas(p.creado, p.primera_revision) for p in revisados if p.primera_revision]),
        "horas_hasta_fusionar_mediana": _mediana([_horas(p.creado, p.fusionado) for p in fusionados if p.fusionado]),
        "con_pruebas": len(con_pruebas),
        "porcentaje_con_pruebas": _porcentaje(len(con_pruebas), n),
        "lineas_de_prueba_mediana": _mediana([float(p.lineas_prueba) for p in fusionados]),
        "revertidos": len(revertidos_aqui),
        "porcentaje_revertidos": _porcentaje(len(revertidos_aqui), n),
    }


def calcular(
    prs: list[PR],
    desde: datetime,
    hasta: datetime,
    regla: str = "auto",
    etiqueta: str = "agente",
    prefijos: tuple[str, ...] = PREFIJOS_POR_DEFECTO,
    costes: dict[int, float] | None = None,
    incluir_bots: bool = False,
) -> dict:
    revertidos = numeros_revertidos(prs)
    bots = [p for p in prs if p.es_bot and not incluir_bots]
    prs = [p for p in prs if incluir_bots or not p.es_bot]
    fusionados = [p for p in prs if p.fusionado and desde <= p.fusionado <= hasta]
    rechazados = [p for p in prs if not p.fusionado and p.cerrado and desde <= p.cerrado <= hasta]

    def agente(p: PR) -> bool:
        return es_de_agente(p, regla, etiqueta, prefijos)

    fus_agente = [p for p in fusionados if agente(p)]
    fus_personas = [p for p in fusionados if not agente(p)]
    resultado = {
        "desde": desde.isoformat(),
        "hasta": hasta.isoformat(),
        "regla": regla,
        "total_fusionados": len(fusionados),
        "porcentaje_de_agente": _porcentaje(len(fus_agente), len(fusionados)),
        "bots_excluidos": len(bots),
        "agentes": _resumen(fus_agente, [p for p in rechazados if agente(p)], revertidos),
        "personas": _resumen(fus_personas, [p for p in rechazados if not agente(p)], revertidos),
        "avisos": [],
    }
    if fus_agente and resultado["agentes"]["revisados"] == 0:
        resultado["avisos"].append(
            "Ningún PR de agente tiene revisiones formales en GitHub (Aprobar o Pedir cambios), así que "
            "«aceptados a la primera» no se puede medir. Mira «commits tras abrir» como señal de correcciones."
        )
    if costes is not None:
        gastos = [costes[p.numero] for p in fus_agente if p.numero in costes]
        resultado["agentes"]["coste"] = {
            "prs_con_coste": len(gastos),
            "total_usd": round(sum(gastos), 2),
            "por_pr_mediana_usd": round(statistics.median(gastos), 2) if gastos else None,
        }
    return resultado


def leer_costes(ruta: Path) -> dict[int, float]:
    """Lee un CSV con columnas ``pr`` (o ``numero``) y ``usd`` (o ``coste_usd``)."""
    costes: dict[int, float] = {}
    with ruta.open(encoding="utf-8", newline="") as fichero:
        for fila in csv.DictReader(fichero):
            numero = fila.get("pr") or fila.get("numero")
            importe = fila.get("usd") or fila.get("coste_usd")
            if numero and importe:
                costes[int(numero)] = costes.get(int(numero), 0.0) + float(importe.replace(",", "."))
    return costes


def a_markdown(resultado: dict) -> str:
    filas = [
        ("PR fusionados", "fusionados"),
        ("Aceptados a la primera (%)", "porcentaje_a_la_primera"),
        ("PR con revisión formal", "revisados"),
        ("Commits tras abrir el PR (mediana)", "commits_tras_abrir_mediana"),
        ("Horas hasta la primera revisión (mediana)", "horas_hasta_primera_revision_mediana"),
        ("Horas hasta fusionar (mediana)", "horas_hasta_fusionar_mediana"),
        ("Cerrados sin fusionar", "cerrados_sin_fusionar"),
        ("Con pruebas (%)", "porcentaje_con_pruebas"),
        ("Líneas de prueba por PR (mediana)", "lineas_de_prueba_mediana"),
        ("Revertidos después (%)", "porcentaje_revertidos"),
        ("Con especificación en el repositorio (%)", "porcentaje_con_especificacion"),
        ("Con nivel de especificación (%)", "porcentaje_con_nivel_de_especificacion"),
    ]

    def celda(valor: object) -> str:
        return "—" if valor is None else str(valor)

    lineas = [
        f"Del {resultado['desde'][:10]} al {resultado['hasta'][:10]} · regla «{resultado['regla']}» · "
        f"{resultado['total_fusionados']} PR fusionados, {celda(resultado['porcentaje_de_agente'])} % de agentes"
        + (f" · {resultado['bots_excluidos']} de bots sin contar" if resultado.get("bots_excluidos") else ""),
        "",
        "| Métrica | Agentes | Personas |",
        "|---|---|---|",
    ]
    for nombre, clave in filas:
        lineas.append(f"| {nombre} | {celda(resultado['agentes'][clave])} | {celda(resultado['personas'][clave])} |")
    coste = resultado["agentes"].get("coste")
    if coste:
        lineas.append(f"| Coste por PR, USD (mediana) | {celda(coste['por_pr_mediana_usd'])} | — |")
    for aviso in resultado.get("avisos", []):
        lineas += ["", f"Aviso: {aviso}"]
    return "\n".join(lineas)


# --- GitHub ---------------------------------------------------------------------------------------


class LimiteDeGitHub(Exception):
    """GitHub ha cortado por límite de peticiones."""


def _fecha(texto: str | None) -> datetime | None:
    return datetime.fromisoformat(texto.replace("Z", "+00:00")) if texto else None


def token_de_github() -> str | None:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token or not shutil.which("gh"):
        return token
    proceso = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
    return proceso.stdout.strip() or None if proceso.returncode == 0 else None


def _get(url: str, token: str | None) -> list | dict:
    peticion = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "agentes-con-control",
    })
    if token:
        peticion.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(peticion, timeout=30) as respuesta:
            return json.loads(respuesta.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        if error.code in (403, 429) and error.headers.get("x-ratelimit-remaining") == "0":
            reinicio = error.headers.get("x-ratelimit-reset")
            cuando = datetime.fromtimestamp(int(reinicio), timezone.utc).strftime("%H:%M UTC") if reinicio else "dentro de un rato"
            raise LimiteDeGitHub(f"GitHub ha cortado por límite de peticiones; se reinicia a las {cuando}") from error
        raise


def _todas(url: str, token: str | None, maximo_paginas: int = 30) -> list:
    elementos: list = []
    separador = "&" if "?" in url else "?"
    for pagina in range(1, maximo_paginas + 1):
        lote = _get(f"{url}{separador}per_page=100&page={pagina}", token)
        elementos.extend(lote)
        if len(lote) < 100:
            break
    return elementos


def descargar(repo: str, desde: datetime, token: str | None) -> list[PR]:
    """PR cerrados desde la fecha, con revisiones, ficheros y commits (unas tres peticiones por PR)."""
    prs: list[PR] = []
    for pagina in range(1, 51):
        lote = _get(f"{API}/repos/{repo}/pulls?state=closed&sort=updated&direction=desc&per_page=100&page={pagina}", token)
        for bruto in lote:
            cerrado = _fecha(bruto.get("closed_at"))
            if not cerrado or cerrado < desde:
                continue
            numero = bruto["number"]
            creado = _fecha(bruto["created_at"])
            usuario = bruto.get("user") or {}
            revisiones = [r for r in _todas(f"{API}/repos/{repo}/pulls/{numero}/reviews", token) if r.get("state") != "PENDING"]
            fechas_revision = sorted(f for f in (_fecha(r.get("submitted_at")) for r in revisiones) if f)
            ficheros = _todas(f"{API}/repos/{repo}/pulls/{numero}/files", token)
            commits = _todas(f"{API}/repos/{repo}/pulls/{numero}/commits", token)
            fechas_commit = [_fecha(((c.get("commit") or {}).get("committer") or {}).get("date")) for c in commits]
            prs.append(PR(
                numero=numero,
                titulo=bruto.get("title", ""),
                autor=usuario.get("login", ""),
                rama=(bruto.get("head") or {}).get("ref", ""),
                etiquetas=[e["name"] for e in bruto.get("labels", [])],
                creado=creado,
                cerrado=cerrado,
                fusionado=_fecha(bruto.get("merged_at")),
                cambios_pedidos=any(r.get("state") == "CHANGES_REQUESTED" for r in revisiones),
                revisado=bool(revisiones),
                primera_revision=fechas_revision[0] if fechas_revision else None,
                lineas_prueba=sum(f.get("additions", 0) for f in ficheros
                                  if FICHERO_DE_PRUEBA.search(f["filename"]) and not f["filename"].startswith(RUTAS_DE_ESPECIFICACION)),
                toca_especificacion=any(f["filename"].startswith(RUTAS_DE_ESPECIFICACION) for f in ficheros),
                lineas_totales=sum(f.get("additions", 0) + f.get("deletions", 0) for f in ficheros),
                mensajes=[(c.get("commit") or {}).get("message", "") for c in commits],
                commits_tras_abrir=sum(1 for f in fechas_commit if f and f > creado),
                es_bot=usuario.get("type") == "Bot" or usuario.get("login", "").endswith("[bot]"),
                cuerpo=bruto.get("body") or "",
            ))
        ultima = _fecha(lote[-1].get("updated_at")) if lote else None
        if len(lote) < 100 or (ultima and ultima < desde):
            break
    return prs


def main(argumentos: list[str] | None = None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    parser = argparse.ArgumentParser(description="Métricas del trabajo de los agentes en un repositorio de GitHub.")
    parser.add_argument("--repo", required=True, help="org/repositorio")
    parser.add_argument("--dias", "--days", type=int, default=30, help="ventana en días (30 por defecto)")
    parser.add_argument("--regla", choices=REGLAS, default="auto", help="cómo se reconoce un PR de agente")
    parser.add_argument("--etiqueta", default="agente", help="etiqueta de los PR de agente")
    parser.add_argument("--prefijos", default=",".join(PREFIJOS_POR_DEFECTO), help="prefijos de rama de agente, separados por comas")
    parser.add_argument("--incluir-bots", action="store_true", help="contar también los PR de bots (Dependabot, Renovate...)")
    parser.add_argument("--costes", type=Path, help="CSV con columnas pr,usd")
    parser.add_argument("--salida", type=Path, help="guardar el resultado en JSON")
    args = parser.parse_args(argumentos)

    token = token_de_github()
    if not token:
        print("Aviso: sin token de GitHub, el límite es de 60 peticiones por hora (unas 3 por PR).", file=sys.stderr)
    hasta = datetime.now(timezone.utc)
    desde = hasta - timedelta(days=args.dias)
    prefijos = tuple(p.strip() for p in args.prefijos.split(",") if p.strip())
    try:
        prs = descargar(args.repo, desde, token)
    except LimiteDeGitHub as error:
        print(str(error), file=sys.stderr)
        return 1
    except urllib.error.HTTPError as error:
        print(f"GitHub respondió {error.code} para {args.repo}: {error.reason}", file=sys.stderr)
        return 1
    costes = leer_costes(args.costes) if args.costes else None
    resultado = calcular(prs, desde, hasta, args.regla, args.etiqueta, prefijos, costes, args.incluir_bots)
    resultado["repo"] = args.repo
    if args.salida:
        args.salida.write_text(json.dumps(resultado, ensure_ascii=False, indent=2), encoding="utf-8")
    print(a_markdown(resultado))
    return 0


if __name__ == "__main__":
    sys.exit(main())
