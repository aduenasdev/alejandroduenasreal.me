# Tasks

## 1. Workflow

- [x] 1.1 Escribir `.github/workflows/ci-cd.yml` con `comprobar`, `desplegar` y `release`, acciones fijadas por SHA; comprobar que el YAML se parsea y que los nombres de pasos coinciden con la spec
- [x] 1.2 Comprobación de enlaces con lychee 0.24.2 (`--offline`, `--root-dir` absoluto); comprobar en local que un enlace roto falla y que el `dist` actual pasa

## 2. Cabeceras y robots

- [x] 2.1 Escribir `public/_headers` y `public/robots.txt`; comprobar que los dos están en `dist/` tras el build
- [ ] 2.2 Comprobar en la vista previa que llegan las cabeceras (`curl -I`) y que no hay errores de CSP en la consola (tras configurar Cloudflare)

## 3. Documentación

- [x] 3.1 README: cómo se despliega, qué hay que preparar una vez en Cloudflare y GitHub y cómo se vuelve atrás; comprobar que los nombres de secretos y entornos coinciden con el workflow
- [x] 3.2 `openspec validate publicacion-automatica --strict` en verde

## Workflow follow-up

- Alejandro prepara Cloudflare y los secretos; un PR de prueba deja la URL de la vista previa.
- Tras el merge: la release aparece en GitHub y `openspec archive publicacion-automatica`.
