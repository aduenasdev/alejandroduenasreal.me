## 1. Contenido

- [x] 1.1 Capítulo de 2024 en `src/data/perfil.ts` con el trabajo y las dos migraciones; mismo texto que el CV

## 2. Comprobación

- [x] 2.1 `astro check`, `npm run build` y `openspec validate --all --strict`; `grep "Java 8" dist/index.html`
- [x] 2.2 El capítulo cabe a 390, 768 y 1440 px, en noche y en día, sin desborde horizontal ni errores de consola (comprobado en producción con Playwright y el Chrome del sistema)
