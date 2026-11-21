# blog Specification

## Purpose

Un blog en español e indexable, con una nota por semana, pensado para reclutadores y responsables técnicos.

## Requirements

### Requirement: Todo en español
El blog SHALL publicarse solo en español: `lang="es"`, textos de la interfaz en español y ninguna ruta en otro idioma.

#### Scenario: Una nota publicada
- **WHEN** se abre `/blog/<slug>/`
- **THEN** la página lleva `lang="es"`, `inLanguage: "es"` en su JSON-LD y no existe ninguna ruta `/en/`

### Requirement: Una nota por semana
El build MUST fallar si dos notas publicadas caen en la misma semana ISO o si dos notas comparten `slug`.

#### Scenario: Dos notas la misma semana
- **WHEN** hay dos notas publicadas con fechas 2026-12-07 y 2026-12-09
- **THEN** `npm run build` falla con el mensaje de la regla, que nombra las dos notas y la semana

#### Scenario: Slug repetido
- **WHEN** dos notas publicadas tienen el mismo `slug`
- **THEN** `npm run build` falla diciendo qué slug está repetido

### Requirement: Borradores
`borrador: true` MUST dejar la nota fuera de las páginas, el RSS y el sitemap. Los ficheros que empiezan por `_` no
se publican.

#### Scenario: Una nota en borrador
- **WHEN** una nota tiene `borrador: true`
- **THEN** no existe su página en `dist/`, ni aparece en el índice, el RSS o el sitemap

### Requirement: Sin notas, sin indexar
Si no hay notas publicadas, el índice del blog SHALL llevar `noindex`, MUST NOT aparecer en el sitemap y el menú
MUST NOT enlazarlo.

#### Scenario: Blog vacío
- **WHEN** no hay notas publicadas
- **THEN** `/blog/` lleva `noindex`, el menú no tiene «Notas» y la portada no tiene la sección Notas

### Requirement: Indexable
Con notas publicadas, el índice y cada nota SHALL ser indexables: sin `noindex`, con `canonical` propio y presentes en
`sitemap.xml`.

#### Scenario: Primera nota publicada
- **WHEN** se publica la primera nota
- **THEN** `/blog/` y `/blog/<slug>/` aparecen en el sitemap y no llevan `noindex`

### Requirement: RSS
SHALL existir `/blog/rss.xml` en RSS 2.0 con las notas publicadas.

#### Scenario: Leer el RSS
- **WHEN** se pide `/blog/rss.xml`
- **THEN** es XML válido con `<language>es</language>` y un `<item>` por nota publicada

### Requirement: Tarjetas
Cada nota SHALL mostrarse en una tarjeta con la portada (o la trama del color de su tipo), el tipo, la serie si la
hay, la fecha corta, los minutos de lectura, el título y la descripción.

#### Scenario: Nota sin portada
- **WHEN** una nota no tiene `portada`
- **THEN** su tarjeta muestra un círculo en trama del color de su tipo

### Requirement: JSON-LD
Cada nota SHALL llevar `BlogPosting` con título, descripción, fecha, idioma, autor y URL.

#### Scenario: Validar el JSON-LD de una nota
- **WHEN** se lee el JSON-LD de una nota
- **THEN** es de tipo `BlogPosting` con `headline`, `description`, `datePublished`, `inLanguage`, `author` y `url`
