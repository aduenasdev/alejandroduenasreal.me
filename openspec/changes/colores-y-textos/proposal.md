# Proposal: colores-y-textos

## Why

Alejandro quiere conservar la composición actual de la web, pero con otra paleta: la de su sistema de diseño (tinta
casi negra, gama de grises y un único verde de señal) en lugar del amarillo sobre negro. También pide nombrar a su
empleador actual, dejar el correo como único contacto (sin CV descargable) y que las cifras coincidan con su CV de
LinkedIn en español, que no se toca.

## What Changes

- Tokens de color de noche y de día en `src/styles/global.css`: fondos, tintas, bordes, el acento `senal` (verde
  menta) y las tres capas (`prod` gris, `lid` tinta, `ia` verde). El foco y el subrayado de los enlaces de día pasan a
  verdes con contraste suficiente. Mismo cambio en el icono (`favicon.svg`) y en la imagen para compartir.
- Textos de `src/data/perfil.ts`: Pangeanic en los dos puestos desde 2024 (sin productos ni clientes); «más de 10
  años» en lugar de 12; fuera «6 equipos y más de 15 personas» de la portada (se queda en la nota del blog); la
  respuesta «¿Ha llevado IA a producción?» nombra Pangeanic y los despliegues en AWS; Vaquify entra en «Trabajo».
- Se quita el botón «CV en PDF». La hoja de impresión se queda.
- `AGENTS.md` y `openspec/config.yaml`: el empleador actual se puede nombrar; sus productos, webs y clientes, no.

## Capabilities

### New Capabilities

- `identidad`: paleta, contacto y datos publicables de la web.

### Modified Capabilities

Ninguna en `openspec/specs/`. Al archivarse, sustituye en `portada` el requisito de no nombrar al empleador y el
escenario «CV en PDF».

## Fuera del alcance

- Composición, tipografías, componentes y movimiento: no cambian.
- La atribución del diseño (Can Aydın, Figma Community) se queda: es obligatoria.
- El CV de LinkedIn no se toca.
- `apple-touch-icon.png` y `og.png` se regeneran con las herramientas de siempre; si no hay navegador local, se dejan
  como tarea pendiente.
