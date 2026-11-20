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

## Despliegue

Lo hace GitHub Actions ([`ci-cd.yml`](.github/workflows/ci-cd.yml)), sin tocar ningún servidor:

1. **Cada PR:** `astro check`, build, `openspec validate --strict` y enlaces internos. Si todo
   pasa, ese mismo `dist` se sube a Cloudflare Pages como **vista previa** y su URL se comenta en el PR.
2. **Al fusionar en `main`:** se repiten las comprobaciones y el `dist` comprobado se despliega en **producción**
   (`https://alejandroduenasreal.me`). Después se crea una release `vAAAA.MM.DD-<sha>` con notas generadas.

Se compila una vez y se despliega ese mismo artefacto: lo que se probó es lo que se publica.

### Preparar una vez (Cloudflare y GitHub)

1. Proyecto de Pages en modo *Direct Upload*: `npx wrangler pages project create alejandroduenasreal --production-branch=main`.
2. Token de API (*My Profile → API Tokens → Custom token*) con **Account · Cloudflare Pages · Edit**.
3. Secretos de Actions: `CLOUDFLARE_API_TOKEN` y `CLOUDFLARE_ACCOUNT_ID`.
4. Entornos de GitHub `vista-previa` y `produccion`.
5. Protección de `main`: PR obligatorio, check `comprobar` en verde, rama al día, sin *force push* ni borrado,
   fusión con rebase o merge commit.
6. Dominio: en *Workers & Pages → alejandroduenasreal → Custom domains*, `alejandroduenasreal.me` y
   `www.alejandroduenasreal.me`; una *Redirect Rule* 301 de `www` a la raíz; *Email Address Obfuscation* apagado.

### Vuelta atrás

- **Normal:** revertir el PR (`git revert -m 1 <merge>`) en un PR nuevo. Al fusionarlo, el circuito despliega la
  versión anterior.
- **Urgente:** *Workers & Pages → alejandroduenasreal → Deployments → Rollback to this deployment* sobre el último
  despliegue bueno. Tarda segundos y no necesita build.

## Diseño

Composición basada en «Graphic Designer Portfolio Homepage» de Can Aydın (Figma Community):
<https://www.figma.com/community/file/1325338426202374850>, con licencia
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.es). Adaptada: colores, textos y componentes propios. El rasgo propio es la impresión risográfica (trama de
puntos) en el retrato, las portadas y los fondos.

## Licencia

El código, con licencia [MIT](LICENSE). Los textos y las imágenes: © 2026 Alejandro Dueñas Real, todos los derechos
reservados.
