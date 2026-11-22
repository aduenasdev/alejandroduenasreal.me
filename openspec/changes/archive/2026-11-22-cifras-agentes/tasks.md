## 1. Cálculo

- [x] 1.1 `scripts/metricas.py` copiado del kit, con la cabecera que dice de dónde sale (se comprueba con `python scripts/metricas.py --help`)
- [x] 1.2 `src/data/agentes.json` generado con `--dias 90 --regla todas` (se comprueba que `agentes.fusionados` coincide con los PR fusionados de GitHub en esas fechas, sin bots)
- [x] 1.3 Paso «Cifras del trabajo con agentes» en `ci-cd.yml`, antes del build, con el token de la ejecución y un aviso en vez de fallo (se comprueba en la ejecución del PR)

## 2. Página

- [x] 2.1 Sección «Medido» en `como-se-hace.astro`, detrás de las comprobaciones, con las seis cifras, el periodo y la explicación de la cifra que falta (se comprueba en la vista previa)
- [x] 2.2 Regla de cifras actualizada en `AGENTS.md` y `openspec/config.yaml`

## 3. Comprobación

- [x] 3.1 `astro check`, `npm run build`, `openspec validate --all --strict` y lychee en verde
- [x] 3.2 Capturas a 390, 768 y 1440 px, en noche y día, sin desbordamiento
