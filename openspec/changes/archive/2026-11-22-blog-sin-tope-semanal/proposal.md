## Por qué

El build falla si dos notas caen en la misma semana ISO. La regla nació para no publicar a golpes, pero ahora frena: si
hay dos notas listas y revisadas, la segunda tiene que esperar a la semana siguiente aunque no haya motivo. Alejandro
quiere quitar ese tope.

## Qué cambia

- **Build (`src/blog.ts`):** ya no falla si dos notas caen en la misma semana. Sigue fallando si dos notas comparten
  `slug`. La función de la semana ISO, que solo servía para esa regla, desaparece.
- **Spec `blog`:**
  - el requisito «Una nota por semana» se sustituye por «Slugs únicos», que deja publicar varias notas la misma semana;
  - el propósito habla de al menos una nota por semana, sin tope.
- **Textos que decían «una nota por semana»:**
  - el subtítulo del blog;
  - la sección «Notas» de la portada;
  - «Cómo se hace»: la comprobación del build, el paso «Publicación» y la lista de reglas;
  - la nota «Hola, soy Alejandro», con su primera regla y su párrafo de qué hay cada semana.

  Pasan a «al menos una nota por semana», sin tope.
- **Reglas del repositorio:** `docs/blog/PLANTILLA.md` (la regla 1 y la fecha, que ya no tiene que ser lunes),
  `AGENTS.md` y `openspec/config.yaml`.

## Qué queda fuera

- **La descripción y la sección «Qué busco» de la nota «Hola, soy Alejandro»:** las cambia el PR #25. Este PR no
  toca esas líneas, para que los dos se puedan fusionar en cualquier orden.
- **Las fechas de las notas ya publicadas.**
- **Un mínimo que haga fallar el build:** «al menos una por semana» es el ritmo que se promete, no una comprobación.
