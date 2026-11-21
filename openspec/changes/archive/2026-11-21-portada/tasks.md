# Tasks

## 1. Contenido

- [x] 1.1 Pasar todo el texto de la portada a `src/data/perfil.ts`; comprobar que los componentes solo llevan encabezados de sección
- [x] 1.2 JSON-LD `Person` con `address` solo de país; comprobar que el JSON del `<script type="application/ld+json">` se parsea y no lleva ciudad

## 2. Portada y cintas

- [x] 2.1 Portada en dos columnas con H1, entrada, botones y `Foto`; comprobar a 1440×900 que todo se ve sin scroll
- [x] 2.2 `Foto` con retrato y monograma de reserva; comprobar que con `retrato.webp` se ve la foto en los dos temas y que sin retratos el build termina y se ve el monograma
- [x] 2.3 `Cintas` cruzadas que se desplazan; comprobar a 390 px que no hay desbordamiento horizontal

## 3. Secciones

- [x] 3.1 «Qué hago» y «Cómo trabajo» con el paso de evaluación en amarillo; comprobar en capturas de noche y día
- [x] 3.2 `Trayectoria` con año en cuentakilómetros, capas cualitativas y columna fija; comprobar con Playwright que los capítulos 3, 4 y 7 dan «2021», «2022» y «Próximo capítulo» con sus capas
- [x] 3.3 «Trabajo» con portadas en trama y cifras huecas; comprobar que las cifras huecas no enseñan contornos internos
- [x] 3.4 `Preguntas` con fuentes numeradas; comprobar que al pulsar la 03 solo se ve su respuesta y `aria-pressed` es correcto
- [x] 3.5 «Formación» con 5 certificados enlazados; comprobar que cada tarjeta abre su URL de verificación
- [x] 3.6 `Contacto`: «Copiar» copia, avisa y no navega; comprobar con Playwright leyendo el portapapeles y la URL

## 4. Accesibilidad, movimiento e impresión

- [x] 4.1 Sin JavaScript: comprobar 7 capítulos al 100 %, 6 respuestas y 0 botones de pregunta
- [x] 4.2 Movimiento reducido: comprobar 0 animaciones en marcha (`document.getAnimations()`)
- [x] 4.3 Teclado: comprobar que el recorrido con Tab enseña el foco en cada elemento
- [x] 4.4 Contraste AA en los dos temas: comprobar el cálculo WCAG de cada par de texto (el más justo, 4,77:1)
- [x] 4.5 Hoja de impresión: comprobar que el PDF en A4 sale en 3 páginas, sin foto, cintas, preguntas ni botones
- [x] 4.6 CLS por debajo de 0,1: comprobar con `PerformanceObserver` (0,000)

## 5. Imagen para compartir

- [x] 5.1 `scripts/og.html` y `public/og.png` de 1200×630 renderizado con Chrome sin ventana; comprobar el tamaño y que el texto se lee

## Workflow follow-up

- Tras el merge de Alejandro: `openspec archive portada`.
- Si llegan versiones del retrato por tema, añadirlas como `src/assets/retrato-noche.*` y `retrato-dia.*`.
