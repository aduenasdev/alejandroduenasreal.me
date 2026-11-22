---
titulo: La ficha técnica de un ingeniero
descripcion: Por qué mi web funciona como una hoja de datos. Cada cifra dice de dónde sale y si está medida o declarada; lo que no se puede comprobar no aparece.
fecha: 2026-11-23
slug: ficha-tecnica-de-un-ingeniero
tipo: opinion
etiquetas: [cifras con fuente, métricas, agentes, transparencia]
borrador: false
---

Nadie compra un regulador de tensión porque el fabricante diga que es «muy eficiente». Se compra porque la hoja de
datos dice qué rendimiento tiene, en qué condiciones se midió y con qué margen. Los perfiles profesionales, en cambio,
están llenos de adjetivos: «apasionado», «orientado a resultados», «experto en IA». Quise que mi web funcionara al revés,
como la ficha técnica de un componente: **cada cifra dice de dónde sale, y lo que no se puede comprobar no aparece.**

## Dos tipos de cifra

No todas las cifras se pueden comprobar igual, así que las separo en dos tipos.

- **Declaradas.** Salen de mi trayectoria y no puedo enseñarte el sistema que las produjo. Lo que sí puedo hacer es que
  sean siempre las mismas, en la web y en mi [CV público de LinkedIn](https://www.linkedin.com/in/aduenasdev), y que no
  haya ninguna más.
- **Medidas.** Las calcula la propia web en cada publicación, a partir de su repositorio público. Cualquiera puede
  repetir el cálculo.

| Cifra | Tipo | De dónde sale |
|---|---|---|
| Más de 45 millones de viajeros al año en la plataforma de billetes que lideré | Declarada | CV de LinkedIn, experiencia en SITRANS |
| 6 equipos y más de 15 personas coordinadas | Declarada | CV de LinkedIn, experiencia en SITRANS |
| 16 PR fusionados en los últimos 90 días, todos con especificación de OpenSpec | Medida | [PR fusionados en GitHub](https://github.com/aduenasdev/alejandroduenasreal.me/pulls?q=is%3Apr+is%3Amerged) |
| 0,7 horas de mediana desde que se abre un PR hasta que lo fusiono | Medida | [El script de métricas](https://github.com/aduenasdev/alejandroduenasreal.me/blob/main/scripts/metricas.py) |
| 0 PR revertidos después | Medida | [Sección «Medido» de «Cómo se hace»](/como-se-hace/) |

Las tres medidas son del 22 de noviembre de 2026. En [Cómo se hace](/como-se-hace/) están siempre las del último despliegue.

## Lo que mide la web

Todos los cambios de esta web los prepara un agente de código y los fusiono yo. La sección «Medido» de «Cómo se hace» recoge
los PR fusionados de los últimos 90 días, sin contar los bots:
- cuántos se fusionaron;
- qué parte trae especificación;
- cuánto tardan en entrar;
- cuántos commits de corrección llevan;
- cuántos se han revertido.

El cálculo no lo hago a mano: lo hace la CI en cada publicación, con la API de GitHub. Si un día GitHub no responde, la
web publica la última foto guardada y la ejecución deja un aviso. Y las cifras solo cambian cuando yo fusiono, porque
mi merge es la aprobación de publicar.

Hay una cifra que **no** enseño: el porcentaje de PR aceptados a la primera. Reviso y fusiono sin marcar «Aprobar» en
GitHub, así que esa cifra, aquí, no existe. Podría inventarla a partir de otras señales; prefiero decir que no la tengo
y enseñar lo más parecido, los commits de corrección.

## Lo que quité

Esta regla deja fuera más de lo que parece. Fuera quedan:
- **Las cifras de proyectos de empresas para las que trabajo o he trabajado**, por buenas que sean: no son mías y no puedo
  enseñarte su fuente.
- **Cualquier número que no esté también en mi CV.** Si no lo sostengo en los dos sitios, no lo sostengo en ninguno.
- **Los adjetivos que no se pueden comprobar.**

Una cifra sin fuente es un adjetivo con números.

## El fallo que encontré en mi propia métrica

Al montar la sección «Medido», mi script dijo que el 62,5 % de los PR traían pruebas. Me extrañó: esta web no tiene
pruebas automáticas. El script contaba como pruebas cualquier fichero dentro de una carpeta `specs/`, y en esta web esas
carpetas son las especificaciones de OpenSpec. Lo corregí y el número bajó a lo que es: **0 % con pruebas y 100 % con
especificación**.

Si hubiera publicado el primer número, nadie lo habría notado. Medir no sirve de nada si no desconfías de tus propias
cifras, y la mejor forma de desconfiar es que cualquiera pueda repetir el cálculo.

## Por qué importa más con agentes

Con agentes de código, producir es barato: una tarde da para diez PR. Lo que se vuelve escaso es la confianza en lo que
se produce. En un equipo, la respuesta no es pedir fe, sino lo mismo que pido a esta web:
- cada cambio con su especificación;
- cada cifra con su fuente;
- las métricas, calculadas por una máquina que no tiene interés en que salgan bonitas.

Es la regla que aplico a cualquier sistema de IA que construyo: **si no hay fuente, no hay respuesta.** Esta web es la
prueba más pequeña que puedo enseñar entera. Si en tu equipo hace falta llevar agentes a producción sin perder el
control, [hablemos](/#hablemos).
