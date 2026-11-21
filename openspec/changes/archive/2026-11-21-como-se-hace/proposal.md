# Proposal: como-se-hace

## Why

Un puesto de agentes en producción y plataforma pide pruebas de que se sabe especificar, comprobar, desplegar y volver
atrás. La web puede enseñarlo entero con su propio circuito y con datos reales de su último despliegue.

## What Changes

- Página `/como-se-hace/` con: datos del último despliegue (commit, fecha del build, ejecución de Actions e insignia),
  el diagrama del circuito, los cuatro pasos y quién decide en cada uno, la tabla de comprobaciones, el workflow real
  leído en el build, la vuelta atrás, cómo nace una nota del blog, el coste y por qué se cuenta.
- Componente `Circuito.astro` (HTML + CSS, sin imágenes).
- Enlaces a la página desde el menú, el pie y la pregunta «¿Sabe desplegar y operar lo que construye?».
- La página entra en el sitemap.
- La CSP permite imágenes de `https://github.com` (la insignia del workflow).

## Capabilities

### New Capabilities

- `como-se-hace`: la página que demuestra el circuito de la web con datos reales.

### Modified Capabilities

Ninguna en specs archivadas. (La spec `publicacion`, aún sin archivar, pide que «Cómo se hace» documente la vuelta
atrás: esta página lo cumple.)

## Fuera del alcance

- Métricas en vivo (duración de builds, historial de despliegues): solo el último despliegue.
- Cloudflare Web Analytics.
- El enlace desde la primera nota (llega con `entrada-bienvenida`).

## Impact

- `src/pages/como-se-hace.astro`, `src/components/Circuito.astro`, `src/env.d.ts`, `Base.astro`, `perfil.ts`,
  `sitemap.xml.ts`, `public/_headers`.
- Usa `PUBLIC_COMMIT` y `PUBLIC_RUN_URL`, que el workflow ya pasa al build.
