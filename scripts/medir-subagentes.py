"""Mide los subagentes de las transcripciones de Claude Code (nota «Lo que vuelve de un subagente»).

Lee ~/.claude/projects/*/*/subagents/*.jsonl y su .meta.json, y escribe una fila por subagente
SIN rutas, prompts ni contenido: tipo, modelo, fecha, contexto máximo, tokens procesados,
número de herramientas y tamaño del informe devuelto.

Uso: python scripts/medir-subagentes.py [carpeta de proyectos] > docs/blog/datos/subagentes.json

- contexto máximo («peak»): la petición más grande (input + caché leída + caché creada + output) según `usage`.
- tokens procesados («total»): suma de esas cantidades en cada petición distinta (cada turno reenvía la conversación).
- informe («inf_tok»): caracteres del informe final entre 4. Es una aproximación, no el tokenizador.
"""
import glob, json, os, sys

base = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/.claude/projects')
filas = []
for f in glob.glob(os.path.join(base, '*', '*', 'subagents', '*.jsonl')):
    meta_p = f[:-6] + '.meta.json'
    meta = json.load(open(meta_p, encoding='utf-8')) if os.path.exists(meta_p) else {}
    pico = total = herr = 0
    vistos, fecha, informe, ultimo_texto = set(), None, None, ''
    for linea in open(f, encoding='utf-8'):
        try:
            o = json.loads(linea)
        except ValueError:
            continue
        fecha = fecha or (o.get('timestamp') or '')[:10] or None
        m = o.get('message') or {}
        if o.get('type') != 'assistant':
            continue
        u = m.get('usage') or {}
        ctx = sum(u.get(k) or 0 for k in ('input_tokens', 'cache_read_input_tokens', 'cache_creation_input_tokens'))
        pico = max(pico, ctx + (u.get('output_tokens') or 0))
        if m.get('id') not in vistos:
            vistos.add(m.get('id'))
            total += ctx + (u.get('output_tokens') or 0)
        for x in m.get('content') or []:
            if x.get('type') == 'tool_use':
                if x.get('name') == 'SubagentHandback':
                    informe = str(x.get('input', {}).get('message', ''))
                else:
                    herr += 1
            elif x.get('type') == 'text' and x.get('text', '').strip():
                ultimo_texto = x['text']
    informe = informe if informe is not None else ultimo_texto
    if pico:
        filas.append(dict(tipo=meta.get('agentType', '?'), modelo=meta.get('model', '?'), fecha=fecha,
                          peak=pico, total=total, herr=herr, inf_tok=round(len(informe) / 4)))
filas.sort(key=lambda r: (r['fecha'] or '', r['tipo'], r['peak']))
json.dump(filas, sys.stdout, ensure_ascii=False, indent=1)
