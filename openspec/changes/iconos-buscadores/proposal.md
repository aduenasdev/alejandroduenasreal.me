## Por qué

Google ya enseña la web en los resultados, pero con el globo genérico en vez del icono «AD». La web solo declaraba
`favicon.svg`; `/favicon.ico` daba 404 y no había ningún PNG cuadrado de un múltiplo de 48 px, que es lo que pide
Google para el icono de los resultados.

## Qué cambia

- `public/favicon.ico` (16, 32 y 48 px) y `public/favicon-192.png` (192 px), generados desde `public/favicon.svg`.
- `Base.astro` declara los tres iconos: ICO, SVG y PNG de 192 px.

## Qué queda fuera

- El diseño del icono.
- Cuánto tarda Google en mostrarlo: lo decide su rastreador de iconos (días o semanas).
