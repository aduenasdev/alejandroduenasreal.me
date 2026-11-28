## 1. Nota

- [x] 1.1 Crear la nota con frontmatter válido (`fecha: 2026-11-28`, `slug: lo-que-vuelve-de-un-subagente`, `tipo: analisis`, `borrador: false`) (se comprueba en `dist/blog/lo-que-vuelve-de-un-subagente/index.html`)
- [x] 1.2 Cada cifra sale de `docs/blog/datos/subagentes-2026-11.json` o lleva fuente enlazada; sin nombres de proyectos, clientes ni empleador (se comprueba recalculando las medianas con el JSON y leyendo la nota)
- [x] 1.3 Portada 1600×900 en WebP, dos tintas de la paleta, sin texto, con `portadaAlt` (se comprueba abriendo la imagen y la tarjeta del blog)

## 2. Comprobación

- [x] 2.1 `npm run check`, `npm run build` y `openspec validate --all --strict --no-interactive` en verde
- [x] 2.2 Capturas de la nota y de `/blog/` a 1440 px (se comprueba mirándolas)
- [x] 2.3 El cambio se archiva en el último commit de este PR antes de abrirlo
