## 1. Implementación

- [x] 1.1 CSP de `public/_headers` con `https://static.cloudflareinsights.com` en `script-src` y `https://cloudflareinsights.com` en `connect-src`

## 2. Comprobación

- [x] 2.1 `astro check`, `npm run build` y `openspec validate --all --strict`; `grep -r cloudflareinsights src dist` solo encuentra `dist/_headers`
- [x] 2.2 Vista previa del PR: las cabeceras llevan la CSP nueva y la consola no muestra errores (en `*.pages.dev` no se inyecta el beacon)
- [ ] 2.3 Tras fusionar y con su sí, quitar el modo «lite» del sitio de Web Analytics de `alejandroduenasreal.me` (ya existe desde el 20-nov con inyección automática, pero «lite» excluye a los visitantes de la UE y no se inyecta en España); en producción el beacon carga sin errores de CSP y el panel registra una visita
