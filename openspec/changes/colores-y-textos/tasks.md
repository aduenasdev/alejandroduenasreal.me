# Tasks

## 1. Colores

- [x] 1.1 Tokens de noche y día, acento, capas y foco en `src/styles/global.css`; comprobar contraste AA del texto con un script
- [x] 1.2 Clases `dia:decoration-prod` a verde y textos sobre acento; comprobar en capturas de noche y día a 390, 768 y 1440 px
- [x] 1.3 `favicon.svg` y `scripts/og.html` sin amarillo; comprobar con `grep ffc72c`

## 2. Textos

- [x] 2.1 Pangeanic, «más de 10 años», sin «6 equipos» en `perfil.ts`; comprobar con `grep`
- [x] 2.2 Respuesta «¿Ha llevado IA a producción?» con Pangeanic y AWS; Vaquify en «Trabajo»; comprobar en la portada
- [x] 2.3 Quitar «CV en PDF»; comprobar que no aparece y que el botón de copiar sigue funcionando
- [x] 2.4 `AGENTS.md` y `openspec/config.yaml` con la nueva regla del empleador

## 3. Comprobación

- [x] 3.1 `astro check`, `npm run build`, `openspec validate --all --strict` y lychee en verde
- [x] 3.2 Vista previa en Cloudflare Pages desde `feat/colores-y-textos`
