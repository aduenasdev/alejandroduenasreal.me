## 1. Dependencias

- [x] 1.1 `astro` 7.4.7, `overrides.vite` 8.3.8 y `engines.node` ≥ 22.23.4 en `package.json`; `npm install` sin conflictos de pares
- [x] 1.2 Trampa de Vite en `AGENTS.md` al día

## 2. Comprobación

- [x] 2.1 `astro check` sin errores ni avisos y `npm run build` sin avisos, con Node 24
- [x] 2.2 `openspec validate --all --strict`
- [x] 2.3 La portada, el blog y «Cómo se hace» generan las mismas páginas que en `main` (comparar la lista de ficheros de `dist/` y el texto de `/`)
- [ ] 2.4 CI del PR en verde; cerrar #8 y #9 como incluidos
