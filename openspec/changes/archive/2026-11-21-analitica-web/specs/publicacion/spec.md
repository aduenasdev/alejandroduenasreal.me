## ADDED Requirements

### Requirement: Analítica de visitas sin cookies
El dominio propio SHALL medir las visitas con Cloudflare Web Analytics, inyectado en el borde de Cloudflare, sin
cookies ni consulta de la URL. La CSP MUST permitir solo `https://static.cloudflareinsights.com` (script) y
`https://cloudflareinsights.com` (envío de datos) como orígenes externos para esa analítica. El repositorio MUST NOT
llevar el script ni el token del beacon, y las vistas previas de `*.pages.dev` MUST NOT medirse.

#### Scenario: CSP preparada para el beacon
- **WHEN** se pide cualquier página del sitio
- **THEN** la CSP lleva `https://static.cloudflareinsights.com` en `script-src` y `https://cloudflareinsights.com` en `connect-src`, y ningún otro origen externo nuevo

#### Scenario: Sin rastro en el repositorio
- **WHEN** se busca `cloudflareinsights` en `src/` y en `dist/`
- **THEN** no aparece: el beacon solo lo añade Cloudflare en el dominio propio
