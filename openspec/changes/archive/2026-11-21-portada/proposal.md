# Proposal: portada

## Why

Un reclutador o un responsable técnico tiene que saber en un vistazo quién es Alejandro, qué hace, cómo ha llegado
hasta aquí y cómo contactarle, con pruebas que pueda comprobar. Hoy la portada es provisional.

## What Changes

- Portada completa en `/`, en este orden: portada con foto, cintas cruzadas, «Qué hago», «Cómo trabajo»,
  «Trayectoria» por capítulos, «Trabajo», «Preguntas con fuente», «Formación» y «Hablemos».
- Todo el texto sale de `src/data/perfil.ts`.
- Componentes: `Foto`, `Cintas`, `Trayectoria` (año que gira como un cuentakilómetros y tres capas cualitativas),
  `Preguntas` (respuestas con fuentes numeradas) y `Contacto` (copiar el correo sin navegar).
- El retrato de Alejandro (`src/assets/retrato.webp`, sin metadatos) en los dos temas; si se quita, un monograma
  en trama risográfica.
- JSON-LD `Person`, hoja de impresión que convierte la portada en un CV de 3 páginas A4 como mucho.
- `og.png` (1200×630) generado con código desde `scripts/og.html`.

## Capabilities

### New Capabilities

- `portada`: la página de inicio, su contenido publicable, temas, accesibilidad, movimiento e impresión.

### Modified Capabilities

Ninguna.

## Fuera del alcance

- La sección «Notas» de la portada y el enlace «Notas» del menú (llegan con el cambio `blog`).
- El enlace «Cómo se hace» del menú, del pie y de la pregunta sobre despliegue apunta a una página que llega con el
  cambio `como-se-hace`; hasta entonces la pregunta enlaza solo al repositorio.
- Versiones del retrato distintas por tema (`retrato-noche` / `retrato-dia`): el componente ya las admite.
- La portada en inglés.

## Impact

- `src/data/perfil.ts`, `src/pages/index.astro`, `src/components/*`, `src/styles/global.css`, `public/og.png`,
  `scripts/og.html`.
