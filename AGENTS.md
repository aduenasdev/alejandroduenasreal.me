# AGENTS.md · alejandroduenasreal.me

Reglas para cualquier agente de IA (o persona) que trabaje en este repositorio. Léelas enteras antes de tocar nada.

## Qué es

Web personal de Alejandro Dueñas Real: diseña y opera agentes de IA en producción (LLMOps y plataforma).
Astro 6 estático + Tailwind CSS 4, sin backend. Todo en español: portada (`/`), blog (`/blog/`) y la
página «Cómo se hace» (`/como-se-hace/`), que enseña con datos reales cómo se especifica, comprueba y despliega la web.
Audiencia: reclutadores y responsables técnicos de equipos de IA y plataforma.

## Proceso: OpenSpec, una rama y un PR por cambio

1. **Todo cambio empieza en OpenSpec.** `npx -y @fission-ai/openspec@2.1.1 new change <id>` y, dentro de
   `openspec/changes/<id>/`: `proposal.md` (por qué, qué y **qué queda fuera**), las specs de cada capacidad
   (`specs/<capacidad>/spec.md`, requisitos con SHALL/MUST y escenarios WHEN/THEN), `design.md` si hay decisiones
   técnicas y `tasks.md` (cada tarea dice **cómo se comprueba**). Un cambio sin comportamiento observable lleva
   `skip_specs: true` en su `.openspec.yaml`.
2. `npx -y @fission-ai/openspec@2.1.1 validate <id> --strict` en verde antes de programar.
3. **Rama corta:** `feat/<id>`, `fix/<id>` o `chore/<id>`. Implementa y marca las tareas `- [x]`.
4. **Commits convencionales en español:** `<tipo>(<ámbito>): <descripción>`, con el trailer
   `OpenSpec-Change: <id>`. Autor: `Alejandro Dueñas <aduenasdev@gmail.com>`, cuenta de GitHub `aduenasdev`.
5. **PR a `main`.** El título se lee en las notas de la release: escríbelo para eso. La CI comenta la URL de la vista
   previa.
6. **Los agentes nunca fusionan, nunca fuerzan un push y nunca borran ramas ni repositorios.** Revisa y fusiona
   Alejandro (rebase o merge commit, nunca squash). Su merge es la aprobación de publicar.
7. Tras el merge: `openspec archive <id>` en un PR pequeño, para que las specs pasen a `openspec/specs/`.

Las specs vigentes están en `openspec/specs/` (`openspec list --specs`). Antes de cambiar un comportamiento, léelas.

## Reglas de contenido (no negociables)

- **Idioma: español (es-ES) en toda la web, blog incluido.** No se publican versiones en otros idiomas.
- **Solo hechos comprobables.** No inventes logros, cifras, puestos, testimonios ni certificados. Lo pendiente se
  dice como pendiente.
- **Empleador actual:** ni el nombre, ni sus productos, ni sus webs, ni sus clientes, ni capturas. Solo «Empresa
  privada» y texto genérico del trabajo.
- **Clientes:** solo **FTChart** puede nombrarse y enlazarse (`https://ftchart.com/`).
- **Puesto:** el actual es el del CV; no se inventan puestos. Ubicación: «España · remoto o híbrido», nunca una ciudad.
- **Nunca:** teléfono, dirección, secretos ni datos de clientes. Sin capturas de productos de terceros.
- La atribución del diseño (Can Aydın, Figma Community) no se quita nunca del pie ni del README.
- Lo que lleva texto exacto (la imagen para compartir, los diagramas) se hace con código, nunca con IA de imágenes.

## Dónde está cada cosa

| Ruta | Qué hay |
|---|---|
| `src/data/perfil.ts` | **Todo** el texto de la portada. Los componentes no llevan texto propio salvo los encabezados de sección |
| `src/layouts/Base.astro` | Cabecera, pie (con la atribución), SEO, script e interruptor de tema |
| `src/styles/global.css` | Tailwind, tokens de noche y día, clases de componente, movimiento reducido e impresión |
| `src/components/` | Componentes de la portada, del blog y del circuito |
| `src/pages/` | Rutas: portada, 404, «Cómo se hace», blog, RSS y sitemap |
| `src/content/blog/` | Notas en Markdown, en español (plantilla en `docs/blog/PLANTILLA.md`) |
| `src/content.config.ts` · `src/blog.ts` | Esquema del blog y sus reglas (una nota por semana ISO) |
| `src/i18n.ts` | Textos de la interfaz del blog |
| `src/assets/` | Retratos opcionales y portadas de las notas |
| `public/` | Icono, `og.png`, `robots.txt` y `_headers` (cabeceras de Cloudflare Pages) |
| `scripts/og.html` | Plantilla de la imagen para compartir (1200×630) |
| `.github/workflows/ci-cd.yml` | Comprobar → desplegar en Cloudflare Pages → release |
| `openspec/` | `config.yaml`, specs vigentes y cambios |

## Diseño, en corto

- Noche por defecto; el día se activa con `data-theme="dia"`. **No uses `dark:`**: usa el variante `dia:`.
- Colores con los tokens (`bg-fondo`, `text-tinta-2`, `bg-senal`…). `prod`, `lid` e `ia` solo en barras y formas,
  nunca en texto pequeño. Todo el texto cumple WCAG AA en los dos temas.
- Rasgo propio: impresión risográfica (clase `.trama`). Nada de rejillas *bento*, *glassmorphism*, terminales falsas,
  degradados morados, neón ni máquinas de escribir.
- Con `prefers-reduced-motion: reduce`, nada se mueve. Sin JavaScript, todo el contenido se ve.

## Cómo comprobar (en cada PR)

```sh
npm ci
npx astro check                     # sin errores ni avisos
npm run build                       # sin avisos
npx -y @fission-ai/openspec@2.1.1 validate --all --strict --no-interactive
npm run preview                     # y revisar a mano
```

Antes de pedir revisión, en la vista previa:
- capturas en móvil (390 px), tableta (768 px) y escritorio (1440 px), en noche y en día: sin desbordamiento horizontal ni errores de consola (CSP incluida);
- teclado: todo se recorre y el foco se ve; `aria-pressed` correcto en los botones de estado;
- sin JavaScript se ven los 7 capítulos y todas las respuestas; con movimiento reducido no hay animaciones;
- imprimir la portada da un CV en blanco y negro de 3 páginas A4 como mucho;
- SEO: `lang="es"`, `canonical`, Open Graph, JSON-LD, sitemap y RSS; nada de `noindex` en páginas publicadas.

## Trampas conocidas

- **Astro:** un `<a>{expresión}</a>` dentro de una celda de tabla hace que el compilador vuelva a abrir el enlace
  después de la tabla. Usa `<a href=… set:text={valor} />`.
- **Astro:** dentro de un fragmento `<>…</>`, un espacio final se recorta. Si hace falta, ponlo como `{' '}`.
- **Astro:** si una nota borrada sigue apareciendo en el build, borra la caché: `rm -rf .astro node_modules/.astro`.
- **Vite:** `@tailwindcss/vite` arrastra Vite 8 y Astro 6 usa Vite 7 (rompe con «Missing field `tsconfigPaths`»).
  `package.json` fija `overrides.vite`; súbelo solo junto con Astro.
- **TypeScript:** `@astrojs/check` admite TypeScript 5 o 6, no 7.
- **Google Fonts:** comprueba el nombre exacto de cualquier fuente nueva; el build avisa con «No data found for font
  family». La fuente condensada «Big Shoulders» no se usa.
- **Tailwind 4:** el tema base es oscuro. No uses `dark:`; usa `dia:`.
