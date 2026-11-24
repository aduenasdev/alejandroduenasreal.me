---
titulo: Las mismas barreras para personas y agentes
descripcion: "Lo que hace seguro dejar trabajar a un agente de código no es el modelo, son las barreras que lo rodean: las mismas que ya pones a las personas."
fecha: 2026-11-24
slug: mismas-barreras-personas-y-agentes
tipo: guia
etiquetas: [agentes, revisión de código, permisos, especificación, métricas]
borrador: false
---

Cuando alguien entra nuevo en un equipo, nadie le da el primer día las claves de producción. Le das una guía con las
reglas del equipo, permiso para leer todo el código, una rama, una plantilla de PR, alguien que revise lo que haga y una
CI que pase las pruebas. Nadie lo llama desconfianza: es como trabaja un equipo.

Con los agentes de código, muchos equipos hacen justo lo contrario. O no los dejan tocar nada, o los dejan hacer de todo
desde el terminal de un desarrollador, con sus permisos. Mi regla es más aburrida: **un agente pasa por las mismas
barreras que una persona.** Ni más, ni menos.

## El problema no es el modelo

Los datos dicen que lo difícil ya no es escribir código, sino fiarse de él:

| Dato | Fuente |
|---|---|
| El 90 % de los profesionales del software usa IA en el trabajo, y un 30 % confía poco o nada en el código que genera | [DORA 2025](https://dora.dev/dora-report-2025/) |
| Al 87 % de los desarrolladores le preocupa la exactitud de los agentes, y al 81 %, la seguridad de los datos | [Stack Overflow 2025](https://survey.stackoverflow.co/2025/ai) |
| En 8,1 millones de PR, los hechos con IA se fusionan en un 32,7 %, frente al 84,4 % de los manuales. Los de agentes esperan 5,3 veces más a que alguien los abra | [LinearB 2026](https://linearb.io/resources/engineering-benchmarks-report) |

Un modelo mejor no arregla eso. Lo arregla saber qué puede hacer el agente y qué no, quién revisa lo que propone y cómo
se nota cuando algo sale mal. Es decir, el entorno en el que trabaja, no el modelo.

## Las barreras, una a una

| Barrera | Para una persona | Para un agente | Quién la hace cumplir |
|---|---|---|---|
| Reglas escritas | La guía del equipo | `AGENTS.md`, que leen Copilot, Codex, Cursor y otros (Claude Code, a través de `CLAUDE.md`) | La revisión |
| Permisos | Leer todo; cambiar con revisión; producción, no | Leer libre; modificar con aprobación; secretos y producción, nunca | La configuración del agente y la de GitHub |
| Secretos | Un gancho de git que mira cada commit | Un hook que mira cada escritura y cada orden | Git, el agente y la CI |
| Especificación | Tanta como riesgo tenga el cambio | La misma | La CI comprueba el nivel |
| Revisión | Un PR que revisa otra persona | Un PR que revisa una persona | La protección de `main` |
| Pruebas | La CI | La misma CI | La CI |
| Vuelta atrás | Un despliegue que se puede deshacer | El mismo | El despliegue |
| Medición | No se mide a las personas | Se miden sus PR: especificación, correcciones y reversiones | Un script sobre la API de GitHub |

Tres detalles que marcan la diferencia:

- **Las barreras fallan cerradas.** Si una comprobación no puede ejecutarse porque falta Python o se agota el tiempo, la
  acción se bloquea, no se deja pasar. Una barrera que el agente se salta cuando falla no es una barrera.
- **Lo dudoso se pregunta.** Entre «siempre» y «nunca» hay un tercer estado: pedir confirmación. `git reset --hard` no
  está prohibido, pero lo confirma una persona.
- **Una persona responde de cada fusión.** El agente propone; una persona revisa, fusiona y responde de lo que entra.

## Por qué las mismas, y no unas especiales para agentes

1. **Un solo juego de reglas.** Si el agente tiene reglas aparte, al mes no coinciden con las del equipo.
2. **Nadie tiene un atajo.** Si la barrera de secretos solo está en el agente, el secreto entra por el commit de una
   persona; si solo está en las personas, entra por el agente. Por eso el mismo comprobador corre en el gancho de git,
   en el hook del agente y en la CI.
3. **Se puede comparar.** Los PR de agentes y los de personas se miden igual, en conjunto y nunca persona a persona.

## Cuánta especificación

No todo cambio necesita un documento. Uso cuatro niveles según el riesgo:
- ninguno para una errata;
- una ficha corta en el PR para un cambio pequeño;
- un cambio de OpenSpec para lo que cambia el comportamiento;
- una decisión con diseño y vuelta atrás, aprobada antes de programar, para lo que toca pagos, datos personales o
  seguridad.

La CI comprueba que cada PR declara el nivel que le toca. Lo cuento con detalle en otra nota.

## En esta web

Esta web es el ejemplo más pequeño que puedo enseñar entero. Todos sus cambios los prepara un agente y pasan por una
especificación de OpenSpec, un PR y la CI. La sección «Medido» de [Cómo se hace](/como-se-hace/) lo cuenta con cifras
que se calculan en cada publicación. El 22 de noviembre de 2026 eran 20 PR fusionados en 90 días, todos con
especificación, y ninguno revertido.

Y enseña también lo que no iba bien. De esos 20 PR, 12 entraron menos de 10 minutos después de abrirse, y uno de
549 líneas entró en 8. Una revisión que encuentra fallos va a unas 400-500 líneas por hora
([SmartBear](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/)); aquello fue un visto bueno.
La revisión es la barrera que antes se rompe cuando el agente es rápido y tú tienes prisa. Así que he cambiado la regla:
ningún PR se fusiona en la misma sesión en que se abre. Lo reviso después, en la vista previa y con el diff delante. La
mediana tardará en notarlo, porque «Medido» mira 90 días atrás.

## Por dónde empezar

No hace falta inventar nada. Empieza por las barreras que ya tienes para las personas y comprueba, una a una, si el
agente pasa por ellas. Mi apuesta es que fallará en tres sitios:
- los permisos, porque el agente usa los del desarrollador;
- los secretos, porque nadie mira lo que escribe;
- la revisión, porque se fusiona sin leer «porque lo ha hecho la IA».

Si quieres contrastarlo con lo que pasa en tu equipo, [hablemos](/#hablemos).
