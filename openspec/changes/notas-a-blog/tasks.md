## 1. Redirección

- [x] 1.1 `public/_redirects` con `/notas` y `/notas/` → `/blog/` 301 (se comprueba que `dist/_redirects` existe tras el build)
- [ ] 1.2 En la vista previa, `/notas` y `/notas/` dan 301 a `/blog/` y `/notas/x` da 404 (se comprueba con curl)

## 2. Comprobación

- [x] 2.1 `npx astro check`, `npm run build` y `openspec validate --all --strict` en verde
- [ ] 2.2 Este PR se archiva con su último commit y lo fusiona Alejandro en otra sesión
