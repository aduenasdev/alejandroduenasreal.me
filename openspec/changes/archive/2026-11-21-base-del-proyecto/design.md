# Design

## Context

Repositorio vacío y web estática sin backend. Los cambios siguientes (portada, blog, «Cómo se hace») se apoyan en
esta base, así que las decisiones de aquí condicionan a todos.

## Goals / Non-Goals

**Goals:**
- Un único sitio para los tokens de diseño y el tema, que cualquier componente use con clases de Tailwind.
- Que un agente que abra el repositorio sepa el proceso y las reglas sin preguntar (`AGENTS.md`).

**Non-Goals:**
- Componentes de la portada o del blog.

## Decisions

- **Tema por atributo, no por `dark:`.** El tema por defecto es la noche; el día se activa con
  `data-theme="dia"` en `<html>` y el variante propio `dia:`. Alternativa descartada: `dark:` de Tailwind, que
  supone el claro como base y obliga a escribir todo al revés.
- **Script del tema en línea en `<head>`.** Evita el destello del tema equivocado antes de pintar. Coste: la CSP
  necesita `'unsafe-inline'` en `script-src` (se documenta en `publicacion-automatica`).
- **Fuentes con la API de Astro (`fontProviders.google()`).** Se descargan en el build y se sirven desde el propio
  dominio, con respaldo métrico ajustado: sin peticiones a Google desde el navegador y sin saltos al cargar.
  Alternativa descartada: `<link>` a Google Fonts (otra petición, otro dominio en la CSP y datos al tercero).
- **TypeScript 6.** `@astrojs/check` admite `^5 || ^6`; la 7 aún no.
- **Licencia:** código MIT; textos e imágenes, todos los derechos reservados (pendiente de confirmar por Alejandro).

## Risks / Trade-offs

- [El build depende de descargar las fuentes] → Si Google Fonts no responde, el build falla y no se publica nada
  roto; se reintenta.
