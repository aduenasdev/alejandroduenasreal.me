# Tasks

## 1. Colección y reglas

- [x] 1.1 Esquema en `src/content.config.ts` (con `z` de `astro/zod`); comprobar que un `titulo` de más de 90 caracteres rompe el build
- [x] 1.2 `src/blog.ts` con la semana ISO y `comprobarReglas()`; comprobar con dos notas del 2026-12-07 y 2026-12-09 que el build falla con «caen en la misma semana (2026-W50)», y con dos slugs iguales que falla con «está repetido»
- [x] 1.3 Borradores; comprobar que una nota con `borrador: true` no aparece en `dist/`, el RSS ni el sitemap

## 2. Páginas

- [x] 2.1 Índice `/blog/` con `noindex` si no hay notas; comprobar el `meta robots` con y sin notas
- [x] 2.2 Página de nota con `BlogPosting` (`inLanguage: es`) y nota anterior/siguiente; comprobar en el HTML generado y que no existe ninguna ruta `/en/`
- [x] 2.3 RSS 2.0 y `sitemap.xml`; comprobar que los dos XML se parsean
- [x] 2.4 `TarjetaNota` con portada o trama del tipo; comprobar en capturas de 390, 768 y 1440 px, noche y día, sin desbordamiento

## 3. Portada y menú

- [x] 3.1 Sección «Notas» y enlace del menú solo con notas publicadas; comprobar que sin notas no aparecen y con una sí
- [x] 3.2 `docs/blog/PLANTILLA.md` con el frontmatter y las reglas; comprobar que el ejemplo pasa el esquema

## Workflow follow-up

- En esta rama el build avisa de que la colección está vacía porque aún no hay notas: desaparece con el cambio `entrada-bienvenida`.
- Tras el merge de Alejandro: `openspec archive blog`.
