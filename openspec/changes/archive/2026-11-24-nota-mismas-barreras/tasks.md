## 1. Nota

- [x] 1.1 Crear `src/content/blog/2026-11-24-mismas-barreras-personas-y-agentes.md` con frontmatter válido (`fecha: 2026-11-24`, `slug: mismas-barreras-personas-y-agentes`, `tipo: guia`, `borrador: false`) y sin menciones ni enlaces al kit privado ni comentarios internos de borrador (se comprueba leyendo el fichero y en `dist/blog/mismas-barreras-personas-y-agentes/index.html`)
- [x] 1.2 Verificar que todas las cifras llevan fuente enlazada y que no hay menciones a empleadores ni clientes privados (se comprueba leyendo el contenido generado)

## 2. Comprobación

- [x] 2.1 `npm run check`, `npm run build` y `openspec validate --all --strict --no-interactive` en verde
- [x] 2.2 El cambio se archiva en el último commit de este PR antes de abrirlo
