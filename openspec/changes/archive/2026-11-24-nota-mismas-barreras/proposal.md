## Por qué

Publicar la nota del método principal de la marca: **un agente de código pasa por las mismas barreras que una persona** (reglas escritas, permisos, secretos, especificación, revisión humana, pruebas, vuelta atrás y medición). Refuerza la sección «Medido» de `/como-se-hace/` con un ejemplo real y honesto (la regla de revisión en frío tras ver que 12 de 20 PR entraron en menos de 10 minutos).

## Qué cambia

Nueva nota en español `src/content/blog/2026-11-24-mismas-barreras-personas-y-agentes.md` (`tipo: guia`, fecha `2026-11-24`, `borrador: false`):

- **Tesis:** lo que hace seguro dejar trabajar a un agente no es el modelo, sino las barreras que lo rodean — las mismas que ya se aplican a las personas.
- **Estructura:**
  1. Apertura (analogía con una persona nueva en un equipo).
  2. *El problema no es el modelo* (tabla con cifras y fuentes).
  3. *Las barreras, una a una* (tabla comparativa persona vs agente + 3 principios: fallar cerrado, preguntar en lo dudoso y una persona responde).
  4. *Por qué las mismas, y no unas especiales para agentes*.
  5. *Cuánta especificación* (los 4 niveles según riesgo).
  6. *En esta web* (cifras reales del 22-11 en «Medido» y regla de revisión en frío).
  7. *Por dónde empezar* (3 fallos habituales + cierre hacia `/#hablemos`).
- **Fuentes verificadas:**
  - [DORA 2025](https://dora.dev/dora-report-2025/)
  - [Stack Overflow 2025](https://survey.stackoverflow.co/2025/ai)
  - [LinearB 2026](https://linearb.io/resources/engineering-benchmarks-report)
  - [SmartBear · Best Practices for Peer Code Review](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/)
  - Datos propios medidos en `/como-se-hace/` (22-11-2026: 20 PR fusionados en 90 días, 100 % con especificación, 0 revertidos, 12 en < 10 min, uno de 549 líneas en 8 min).

## Qué queda fuera

- **El kit `agentes-con-control`:** sigue privado, así que la nota no lo nombra ni lo enlaza. El enlace se añadirá en un PR aparte cuando sea público.
- **Portada ilustrada:** la tarjeta usa la trama del tipo `guia`.
- **Cambios en otras páginas o en el esquema del blog.**
