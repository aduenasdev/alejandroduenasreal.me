# Proposal: entrada-bienvenida

## Why

El blog necesita su primera nota: quién es Alejandro, qué busca, cómo leer la web y las reglas con las que escribe.
Es también la que enlaza «Cómo se hace» y el repositorio, así que solo puede publicarse cuando lo que cuenta sea cierto.

## What Changes

- Nota en español `src/content/blog/2026-11-23-hola-soy-alejandro.md` (`/blog/hola-soy-alejandro/`), `tipo: opinion`.
- Con `borrador: true`.

## Capabilities

### New Capabilities

Ninguna: es contenido sobre la capacidad `blog` (`skip_specs: true`).

### Modified Capabilities

Ninguna.

## Fuera del alcance

- Publicarla. Se publica en un PR aparte que solo cambia `borrador: true` por `false` cuando se cumplan las tres
  condiciones: el repositorio es público, cada cambio empieza con OpenSpec y la web se despliega sola en Cloudflare
  Pages. Si sale después del 2026-11-23, la `fecha` pasa al lunes de esa semana.
- La portada ilustrada (opcional; sin ella, la tarjeta muestra la trama amarilla de «Opinión»).

## Impact

- Un fichero nuevo en `src/content/blog/`. Mientras sean borrador, no cambia ninguna página publicada.
