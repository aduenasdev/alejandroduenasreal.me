## 1. Implementación

- [x] 1.1 CSP de `public/_headers` con `https://static.cloudflareinsights.com` en `script-src` y `https://cloudflareinsights.com` en `connect-src`

## 2. Comprobación

- [x] 2.1 `astro check`, `npm run build` y `openspec validate --all --strict`; `grep -r cloudflareinsights src dist` solo encuentra `dist/_headers`
- [ ] 2.2 Vista previa del PR: las cabeceras llevan la CSP nueva y la consola no muestra errores
- [ ] 2.3 Tras fusionar y con su sí, Web Analytics activado en Cloudflare para `alejandroduenasreal.me` con inyección automática; en producción el beacon carga sin errores de CSP y el panel registra una visita
