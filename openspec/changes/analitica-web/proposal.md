## Por qué

Alejandro quiere saber cuántas visitas llegan a la web y cuántas vienen de LinkedIn (destacado, contacto y posts),
sin cookies ni banner de consentimiento.

## Qué cambia

- **Cloudflare Web Analytics** con inyección automática en el borde de Cloudflare, solo en el dominio propio
  (`alejandroduenasreal.me`, con proxy). No hay código ni token en el repositorio y las vistas previas de
  `*.pages.dev` no se miden. Web Analytics no usa cookies ni guarda la consulta de la URL ni datos personales.
- La CSP de `public/_headers` permite solo lo que necesita el beacon: `https://static.cloudflareinsights.com` en
  `script-src` y `https://cloudflareinsights.com` en `connect-src`.
- El origen de las visitas se ve en el panel (*Referer*: `www.linkedin.com`, `lnkd.in`, `com.linkedin.android`…).

## Qué queda fuera

- Parámetros `utm_`: Web Analytics no guarda la consulta de la URL, así que no se usarían.
- Un contador visible en la página, eventos propios y cualquier analítica con cookies.
- Activar Web Analytics en Cloudflare: es configuración de la cuenta y se hace después de fusionar, con el sí de
  Alejandro (si se activa antes, la CSP vieja bloquea el beacon y la consola muestra errores).
