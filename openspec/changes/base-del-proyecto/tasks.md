# Tasks

## 1. Proyecto

- [x] 1.1 Crear `package.json` con `astro`, `tailwindcss` y `@tailwindcss/vite` fijados, `@astrojs/check` y `typescript` como desarrollo; comprobar que `npm ci` instala sin avisos de pares
- [x] 1.2 Crear `astro.config.mjs` (sitio, i18n, fuentes, Tailwind), `tsconfig.json` y `.node-version`; comprobar que `npm run build` genera `dist/index.html`

## 2. Diseño base

- [x] 2.1 Escribir `src/styles/global.css` con los tokens de noche y día, el variante `dia:`, las clases de componente y los estilos base; comprobar en el navegador que el fondo es `#121212` en noche y `#f3f3f0` en día
- [x] 2.2 Escribir `src/layouts/Base.astro` (cabecera, pie con la atribución, SEO, script del tema e interruptor); comprobar que el tema elegido sobrevive a una recarga y que el pie enlaza a la plantilla de Figma
- [x] 2.3 Añadir `public/favicon.svg` y `src/pages/404.astro`; comprobar que `dist/404.html` existe y que el icono se ve en la pestaña

## 3. Reglas y documentación

- [x] 3.1 Escribir `AGENTS.md` (proceso, reglas de contenido, mapa, comprobaciones y trampas) y `CLAUDE.md` con `@AGENTS.md`; comprobar que `CLAUDE.md` contiene solo esa línea
- [x] 3.2 Escribir `README.md` (qué es, cómo arrancar, atribución y licencia) y `LICENSE`; comprobar que la atribución del diseño aparece en el README
- [x] 3.3 Pasar `npx astro check` y `npm run build` sin avisos, y `openspec validate base-del-proyecto --strict`

## Workflow follow-up

- Tras el merge de Alejandro: `openspec archive base-del-proyecto`.
