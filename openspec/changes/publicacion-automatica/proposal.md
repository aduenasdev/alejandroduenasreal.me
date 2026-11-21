# Proposal: publicacion-automatica

## Why

La web tiene que demostrar lo que dice: que un cambio, lo escriba una persona o un agente, no llega a producción sin
comprobaciones automáticas y sin la aprobación de Alejandro. Hoy no hay CI ni despliegue: publicar sería un paso
manual que no se puede auditar.

## What Changes

- Workflow `.github/workflows/ci-cd.yml` con tres trabajos:
  - `comprobar`: `astro check`, build, `openspec validate --all --strict` y comprobación de enlaces internos con
    lychee. Guarda `dist` como artefacto.
  - `desplegar`: sube **ese mismo** `dist` a Cloudflare Pages. En un PR, vista previa con su URL comentada en el PR;
    en `main`, producción.
  - `release`: tras cada despliegue a producción, una release `vAAAA.MM.DD-<sha>` con notas generadas.
- `public/_headers`: cabeceras de seguridad y `noindex` en `*.pages.dev`.
- `public/robots.txt` con el sitemap.
- README: cómo se despliega y cómo se vuelve atrás.

## Capabilities

### New Capabilities

- `publicacion`: comprobación, vista previa, despliegue a producción, release, vuelta atrás y cabeceras.

### Modified Capabilities

Ninguna.

## Fuera del alcance

- Crear el proyecto de Cloudflare Pages, el token, los secretos de GitHub, la protección de `main` y el dominio:
  lo hace Alejandro (o un agente con su permiso) fuera del repositorio. Los pasos están en el README.
- Pruebas visuales automáticas (Playwright) en la CI: se hacen a mano en cada PR, según `AGENTS.md`.
- Web Analytics.

## Impact

- Ficheros nuevos: `.github/workflows/ci-cd.yml`, `public/_headers`, `public/robots.txt`.
- Necesita los secretos `CLOUDFLARE_API_TOKEN` y `CLOUDFLARE_ACCOUNT_ID`, y los entornos `vista-previa` y
  `produccion`.
