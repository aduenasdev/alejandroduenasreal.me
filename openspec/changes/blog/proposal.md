# Proposal: blog

## Why

Una nota por semana, con datos y fuentes, es la forma de enseñar criterio sobre IA en producción a reclutadores y
responsables técnicos. Tiene que ser indexable, en español, y con una regla que impida publicar a golpes.

## What Changes

- Colección `blog` en `src/content/blog/` con esquema (título, descripción, fecha, slug, tipo, serie, portada,
  etiquetas, borrador).
- Reglas en el build: una nota por semana ISO y sin slugs repetidos (si no, falla); borradores fuera.
- Páginas: índice en `/blog/`, cada nota en `/blog/<slug>/`, RSS 2.0 en `/blog/rss.xml` y `sitemap.xml`.
- Tarjeta de nota (portada o trama del color de su tipo), sección «Notas» en la portada y enlace «Notas» en el menú,
  solo cuando hay notas publicadas.
- `docs/blog/PLANTILLA.md` para escribir una nota.

## Capabilities

### New Capabilities

- `blog`: publicación de notas en español, sus reglas, su indexación y su presentación.

### Modified Capabilities

Ninguna. (La sección «Notas» de la portada ya está prevista en la spec `portada`, requisito «Orden de secciones».)

## Fuera del alcance

- Versiones en otros idiomas: decisión de Alejandro, toda la web y el blog en español.
- La primera nota (cambio `entrada-bienvenida`).
- Comentarios, búsqueda, etiquetas navegables y paginación (con pocas notas no hacen falta).

## Impact

- `src/content.config.ts`, `src/blog.ts`, `src/rss.ts`, `src/pages/blog/*`, `src/pages/sitemap.xml.ts`,
  `src/components/{TarjetaNota,ListaBlog,EntradaBlog}.astro`, `Base.astro`, `index.astro`, `global.css`.
