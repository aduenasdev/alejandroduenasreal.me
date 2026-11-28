## Por qué

Hay quien escribe `/notas` a mano o lo deduce del texto de la web, porque las entradas del blog se llaman «notas».
Hoy esa ruta da 404. Una herramienta de revisión externa la probó y la dio por bloqueada.

## Qué cambia

- `public/_redirects` con `/notas` y `/notas/` → `/blog/` (301). Cloudflare Pages lo aplica en el borde.
- Spec `blog`: requisito nuevo «Ruta /notas».

## Qué queda fuera

- Las notas sueltas (`/notas/<slug>`): no han existido nunca, así que siguen dando 404.
- Cambiar el nombre de `/blog/` o el del menú.
