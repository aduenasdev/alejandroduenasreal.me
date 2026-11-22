## 1. Nota

- [x] 1.1 Descripción sin «qué busco» (se comprueba en la tarjeta de la nota, en la portada y en `/blog/`)
- [x] 1.2 Sección «Hacia dónde voy» en lugar de «Qué busco», sin nombrar un puesto (se comprueba en `/blog/hola-soy-alejandro/`)
- [x] 1.3 Ni la nota ni su tarjeta dicen ya «busco» (se comprueba en `dist/blog/hola-soy-alejandro/index.html` y en `dist/index.html`, donde el único «busco» que queda es el del próximo capítulo, que quita el PR #24)

## 2. Comprobación

- [x] 2.1 `npm run check`, `npm run build` y `openspec validate --all --strict` en verde
- [x] 2.2 El cambio se archiva en el último commit de este PR
