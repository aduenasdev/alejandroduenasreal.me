## 1. Implementación

- [x] 1.1 `favicon.ico` (16/32/48) y `favicon-192.png` generados desde `favicon.svg` con PyMuPDF y Pillow
- [x] 1.2 `Base.astro` con los tres `rel="icon"`

## 2. Comprobación

- [x] 2.1 `astro check`, `npm run build` y `openspec validate --all --strict`; los tres iconos están en `dist/` y en el `<head>`
- [ ] 2.2 En producción, las tres URL responden 200; volver a pedir la indexación de `/` en Search Console
