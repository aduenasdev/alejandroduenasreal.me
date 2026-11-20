# Proposal: base-del-proyecto

## Why

El repositorio nace vacío. Antes de construir la portada, el blog o el circuito de despliegue hace falta una base
común: el framework, los estilos, las fuentes, los idiomas, la estructura de carpetas y las reglas que leen los
agentes que trabajan en el repositorio.

## What Changes

- Proyecto **Astro 6** estático con **Tailwind CSS 4** (`@tailwindcss/vite`), dependencias con versión fija.
- Fuentes **Sora** y **Atkinson Hyperlegible Next** servidas desde el propio dominio con la API de fuentes de Astro.
- i18n: español en la raíz y el inglés bajo `/en/`.
- Tokens de diseño (noche por defecto y modo día con el variante `dia:`), clases de componente y estilos base.
- `Base.astro`: cabecera, pie con la atribución del diseño, SEO común e interruptor de tema que se recuerda.
- Icono «ad.» (`public/favicon.svg`), página 404 y una portada provisional.
- `AGENTS.md` (proceso, reglas de contenido, mapa del repositorio, cómo comprobar y trampas conocidas),
  `CLAUDE.md` (solo `@AGENTS.md`), `README.md`, `LICENSE` y `.node-version`.

## Capabilities

### New Capabilities

Ninguna. Es andamiaje: no hay comportamiento observable que especificar todavía (`skip_specs: true`).

### Modified Capabilities

Ninguna.

## Fuera del alcance

- La CI y el despliegue (cambio `publicacion-automatica`).
- El contenido de la portada (cambio `portada`), el blog (`blog`) y «Cómo se hace» (`como-se-hace`).
- La portada en inglés.

## Impact

- Ficheros nuevos en la raíz, `src/` y `public/`.
- Dependencias: `astro`, `tailwindcss`, `@tailwindcss/vite`, `@astrojs/check`, `typescript`.
- Node 22.12 o superior; la CI usará la versión de `.node-version` (24).
