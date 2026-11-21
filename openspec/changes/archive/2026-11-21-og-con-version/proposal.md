## Por qué

LinkedIn y otras redes guardan en caché la imagen para compartir por su URL. `og.png` cambió el 21-nov (titular
nuevo), pero la URL sigue siendo `/og.png`, y el Post Inspector de LinkedIn vuelve a leer la página y sigue
enseñando la imagen vieja.

## Qué cambia

- `og:image` y la `image` del JSON-LD llevan una versión sacada del contenido de `public/og.png`
  (`/og.png?v=<8 primeros caracteres del SHA-256>`). Si la imagen cambia, cambia la URL; si no cambia, la URL es la
  misma en cada build.

## Qué queda fuera

- El diseño y el texto de la imagen.
- Renombrar el fichero: `/og.png` sigue sirviéndose igual.
