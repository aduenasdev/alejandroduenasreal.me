# Tasks

## 1. Nota

- [x] 1.1 Escribir la nota en español con `borrador: true`; comprobar que el build no genera `/blog/hola-soy-alejandro/` ni la sección «Notas»
- [x] 1.2 Comprobar con `borrador: false` en local que: la página existe con `lang="es"`, el RSS tiene un `<item>`, el sitemap la incluye sin `noindex`, la portada muestra «Notas» y lychee no encuentra enlaces rotos
- [x] 1.3 Revisar que cada dato de la nota coincide con `src/data/perfil.ts` (6 equipos, más de 15 personas, 45 M de viajeros, desde 2014, FTChart) y que no nombra al empleador actual

## 2. Publicación (PR aparte, cuando sea cierto lo que cuenta)

- [x] 2.1 Repositorio público y despliegue automático funcionando; comprobar en `/como-se-hace/` el commit del último merge
- [x] 2.2 Cambiar `borrador: true` por `false` (y la `fecha` al lunes de esa semana si hace falta); comprobar la nota en la vista previa del PR

## Workflow follow-up

- Tras publicar: `openspec archive entrada-bienvenida`.
