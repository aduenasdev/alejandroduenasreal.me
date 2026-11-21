## 1. Implementación

- [x] 1.1 `src/og.ts` con la URL versionada; `Base.astro` y el JSON-LD de `index.astro` la usan

## 2. Comprobación

- [x] 2.1 `astro check`, `npm run build` y `openspec validate --all --strict`; comprobar con `sha256sum public/og.png` que la versión de `dist/index.html` coincide
- [ ] 2.2 Tras desplegar, el Post Inspector de LinkedIn enseña la imagen nueva
