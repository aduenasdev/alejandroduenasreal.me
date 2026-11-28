---
titulo: "Lo que vuelve de un subagente: 40 delegaciones medidas"
descripcion: "Medí 40 subagentes de mis sesiones reales de Claude Code. Cargaron una mediana de 118.500 tokens y devolvieron unos 1.880. Y cuándo delegar no ahorra nada."
fecha: 2026-11-28
slug: lo-que-vuelve-de-un-subagente
tipo: analisis
serie: Agentes en producción
portada: ../../assets/blog/lo-que-vuelve-de-un-subagente.webp
portadaAlt: "Ilustración risográfica en verde y gris: un archivo enorme de estanterías y una sola nota pequeña que viaja por un camino de puntos hasta un escritorio."
etiquetas: [agentes, subagentes, contexto, Claude Code, métricas]
borrador: false
---

Cuando un agente de código lee una página web, un log o veinte ficheros para contestar una pregunta, todo eso se queda
en su conversación. La respuesta ocupa tres líneas; lo leído, cien mil tokens. Y lo leído sigue ahí en cada turno
siguiente, ocupando sitio y costando dinero.

Un subagente cambia eso. Hace la lectura en su propia ventana de contexto y solo devuelve el informe final. Así lo
explica la [documentación de Claude Code](https://code.claude.com/docs/en/sub-agents): el subagente trabaja en su propio
contexto y devuelve solo el resumen.

Quería saber cuánto vale eso de verdad, no en un ejemplo de juguete. Así que medí mis propias sesiones.

## Qué medí

Todas las delegaciones que guardan las transcripciones de Claude Code en mi equipo, del 29 de octubre al 28 de
noviembre de 2026: **40 subagentes en 14 sesiones** de trabajo real (webs, revisiones, documentación, búsqueda de
información).

- **Contexto máximo:** la petición más grande que hizo el subagente (entrada, caché incluida, más salida), según el
  campo `usage` de cada respuesta.
- **Tokens procesados:** la suma de todas sus peticiones. Cada turno vuelve a enviar la conversación, así que esta cifra
  crece mucho más rápido que el contexto.
- **Informe:** lo que el subagente devolvió a la conversación principal. Lo estimo en caracteres entre 4; es una
  aproximación, no el tokenizador.

El [script que lo mide](https://github.com/aduenasdev/alejandroduenasreal.me/blob/main/scripts/medir-subagentes.py)
y los [datos, una fila por subagente](https://github.com/aduenasdev/alejandroduenasreal.me/blob/main/docs/blog/datos/subagentes-2026-11.json),
están en el repositorio de esta web. Las filas no llevan rutas, encargos ni contenido: solo tipo, modelo, fecha y tokens.

## Lo que salió

| Tipo de subagente | Delegaciones | Contexto máximo (mediana) | Informe (mediana) | Proporción |
|---|---|---|---|---|
| Leer páginas web (`web-fetch`) | 32 | 113.700 tokens | 1.830 tokens | 69 a 1 |
| Explorar código o investigar (`Explore`, `general-purpose`) | 5 | 143.600 tokens | 2.490 tokens | 58 a 1 |
| **Todos menos los forks** | **37** | **118.500 tokens** | **1.880 tokens** | **68 a 1** |
| Forks (heredan la conversación) | 3 | 484.900 tokens | 1.130 tokens | 433 a 1 |

En los 37 subagentes normales:

- el contexto máximo fue de 10.300 a 487.200 tokens (la mitad, entre 44.200 y 193.700);
- el informe nunca pasó de unos 4.200 tokens;
- 36 de 37 devolvieron al menos 20 veces menos de lo que cargaron;
- 21 pasaron de 100.000 tokens de contexto, y 9, de 200.000. Sin delegar, cada uno de esos 9 habría ocupado gran parte
  de la ventana principal.

## Lo que no es gratis

Delegar no ahorra tokens; los mueve. La mediana de tokens procesados por un subagente normal fue de 360.300, y la de
los forks, de 22,1 millones. Esa cifra es tan grande porque cada turno vuelve a leer toda la conversación, y la mayoría
son lecturas de caché, que se cobran más baratas.

Lo que sí gana la conversación principal es sitio: recibe unos 1.880 tokens en lugar de 118.500. Y cada turno siguiente
cuesta menos, porque no arrastra lo leído.

Hay dos detalles que cambian la cuenta:

1. **El modelo del subagente.** Los 32 subagentes de lectura web corrieron en Haiku, el modelo pequeño. La documentación
   lo propone así para [controlar costes](https://code.claude.com/docs/en/sub-agents). Leer y resumir una página no
   necesita el modelo grande.
2. **El fork no empieza vacío.** Un fork [hereda toda la conversación](https://code.claude.com/docs/en/sub-agents#fork-the-current-conversation)
   hasta ese momento. Mis tres forks arrancaron por encima de 400.000 tokens y procesaron entre 18,7 y 48,5 millones. La
   ventana principal se protege igual, pero el fork paga todo el contexto en cada turno. Solo compensa cuando el trabajo
   necesita de verdad todo lo hablado.

## Cómo delego ahora

- **Delego la lectura, no la decisión.** El subagente lee la página, el log o el repositorio y devuelve lo que encontró.
  La conclusión la saco yo en la conversación principal, que tiene el contexto del problema.
- **El encargo dice qué tiene que volver.** El subagente solo sabe lo que pone en su encargo. Así que el encargo dice
  qué buscar, qué formato quiero y cuánto puede ocupar («máximo unas 350 palabras»). Un informe largo es lo que
  queríamos evitar.
- **Fork solo cuando el contexto es imprescindible.** Si el encargo se puede explicar en un párrafo, es un subagente
  normal.
- **Lo que vuelve es un resumen, no la fuente.** Si una cifra del informe importa, la compruebo en el original antes de
  usarla. El resumen puede equivocarse, y yo no he leído lo que leyó el subagente.

## Lo que no medí

- **La calidad de los informes.** No tengo un criterio automático de acierto: los leí y los usé, pero no los he puntuado.
- **Qué habría pasado sin delegar.** No repetí las tareas sin subagente. La proporción de 68 a 1 dice cuánto sitio se
  ahorró la ventana principal, no cuánto mejor o peor salió el resultado.
- **El coste en euros.** Las cifras son tokens. El precio depende del modelo y de cuánto es caché, y no lo he separado.

Si quieres la comparación controlada, con y sin subagente, diez ejecuciones por caso y un modelo local,
[Pablo Melero la hizo en su serie sobre un asistente de código local](https://pablomeleroalonso.me/blog/delegar-no-es-paralelizar/):
en su prueba, delegar costó un 57 % más de tokens y dejó el contexto del agente principal en menos de la mitad. Mis
datos son la otra cara: sin control, pero de trabajo real.

Si tú también mides cómo trabajan tus agentes, [hablemos](/#hablemos).
