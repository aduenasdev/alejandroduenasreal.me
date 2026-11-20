# Design

## Context

Sitio estático (`dist/`) sin backend. GitHub Actions es gratis en repositorios públicos y Cloudflare Pages en modo
*Direct Upload* también. El DNS del dominio ya está en Cloudflare.

## Goals / Non-Goals

**Goals:**
- Lo que se probó es lo que se publica: compilar una vez y desplegar ese artefacto.
- Que nada llegue a producción sin pasar por un PR fusionado por Alejandro.

**Non-Goals:**
- Despliegues desde forks (no tienen secretos y no se despliegan).

## Decisions

- **Cloudflare Pages en *Direct Upload*, sin conectar Git.** Así el build lo hace la CI, no Cloudflare, y el mismo
  `dist` que pasó las comprobaciones es el que se sube. Alternativa descartada: la integración Git de Pages, que
  compila otra vez por su cuenta. Otra descartada: el VPS compartido, que expone su IP al origen, no da vistas
  previas por PR y obliga a guardar una clave SSH en GitHub.
- **Acciones fijadas por SHA**, con la versión en un comentario. Una etiqueta se puede mover; un SHA no.
- **Wrangler fijado** (`wranglerVersion`) para que un despliegue no cambie de comportamiento solo.
- **lychee sin red (`--offline`)** y con `--root-dir` absoluto: solo enlaces internos. Los externos no rompen un PR
  por una caída ajena.
- **URL de la vista previa:** se comenta el alias de la rama (`<rama>.alejandroduenasreal.pages.dev`) si existe, y si
  no la URL del despliegue. Cloudflare marca las vistas previas con `noindex` por su cuenta; `_headers` añade además
  `noindex` a `alejandroduenasreal.pages.dev`.
- **Permisos mínimos:** `contents: read` por defecto; `pull-requests: write` y `deployments: write` solo en
  `desplegar`; `contents: write` solo en `release`.

## Risks / Trade-offs

- [`cancel-in-progress` en `main` podría cortar un despliegue] → Se acepta: el siguiente push despliega su propio
  artefacto completo, que es más nuevo.
- [La CSP necesita `'unsafe-inline'` en `script-src` por el script del tema en `<head>`] → Es un script fijo, sin
  datos del usuario; se revisa si alguna vez se añade contenido de terceros.
- [Sin los secretos de Cloudflare, el trabajo `desplegar` falla] → `comprobar` sigue pasando; solo falta la vista previa.

## Migration Plan

1. Alejandro crea el proyecto de Pages, el token y los secretos (README).
2. Un PR de prueba comprueba la vista previa; al fusionar, se mueve el dominio al proyecto de Pages.
3. Vuelta atrás: revert del PR o *Rollback* en Cloudflare (README y «Cómo se hace»).
