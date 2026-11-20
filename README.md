# alejandroduenasreal.me

Web personal de **Alejandro Dueñas Real**: diseño y opero agentes de IA en producción (LLMOps y plataforma).

👉 **https://alejandroduenasreal.me**

La propia web es una prueba pequeña y completa de cómo trabajo con agentes: cada cambio empieza con una
especificación en [OpenSpec](https://github.com/Fission-AI/OpenSpec), se programa con agentes de IA, se comprueba en
CI y se despliega solo, con vista previa por PR y vuelta atrás.

## Stack

- [Astro 6](https://astro.build) estático, sin backend.
- [Tailwind CSS 4](https://tailwindcss.com) con `@tailwindcss/vite`.
- Fuentes Sora y Atkinson Hyperlegible Next, servidas desde el propio dominio.

## Arrancar en local

Necesitas Node 22.12 o superior (la CI usa la versión de `.node-version`).

```sh
npm ci
npm run dev        # http://localhost:4321
npm run build      # genera dist/
npx astro check    # tipos
```

## Cómo se trabaja

El proceso, las reglas de contenido, el mapa del repositorio y cómo comprobar cada cambio están en
[AGENTS.md](AGENTS.md). Las especificaciones viven en [`openspec/`](openspec/).

## Diseño

Diseño basado en «Graphic Designer Portfolio Homepage» de Can Aydın (Figma Community):
<https://www.figma.com/community/file/1325338426202374850>. El rasgo propio es la impresión risográfica (trama de
puntos) en el retrato, las portadas y los fondos.

## Licencia

El código, con licencia [MIT](LICENSE). Los textos y las imágenes: © 2026 Alejandro Dueñas Real, todos los derechos
reservados.
