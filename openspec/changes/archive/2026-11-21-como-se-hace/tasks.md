# Tasks

## 1. Página

- [x] 1.1 Cabecera y franja de datos del despliegue con `PUBLIC_COMMIT` y `PUBLIC_RUN_URL`; comprobar que un build con `PUBLIC_COMMIT=0123456…` enseña «0123456» enlazado y que en local enseña «local»
- [x] 1.2 `Circuito.astro` en serpentina (escritorio) y en columna (móvil); comprobar en capturas a 390 y 1440 px sin desbordamiento
- [x] 1.3 Los cuatro pasos con «El agente» y «Yo»; comprobar que «Publicar» dice que el agente nunca fusiona
- [x] 1.4 Tabla de comprobaciones, workflow real con `?raw`, vuelta atrás, ciclo de una nota y coste; comprobar que el bloque de código coincide con `.github/workflows/ci-cd.yml`

## 2. Enlaces y cabeceras

- [x] 2.1 Enlaces desde el menú, el pie y la pregunta de despliegue, y entrada en el sitemap; comprobar con lychee (`--offline`) que no hay enlaces rotos
- [x] 2.2 CSP con `img-src https://github.com` para la insignia; comprobar inyectando la cabecera de `_headers` con Playwright que no hay errores de consola en `/`, `/como-se-hace/`, `/blog/` y `/404.html`
- [ ] 2.3 Comprobar en producción que la insignia carga y que el commit es el del último merge (necesita el repositorio público y el despliegue configurado)

## Workflow follow-up

- Tras el merge de Alejandro: `openspec archive como-se-hace`.
