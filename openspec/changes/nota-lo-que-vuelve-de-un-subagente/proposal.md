## Por qué

Una nota de análisis con datos propios sobre cómo se comporta la delegación en subagentes en trabajo real con Claude
Code. Encaja con la marca (agentes en producción, medidos) y estrena la primera portada ilustrada del blog, hecha con
código en el estilo risográfico de la web.

## Qué cambia

- Nota nueva `src/content/blog/2026-11-28-lo-que-vuelve-de-un-subagente.md` (`tipo: analisis`, serie «Agentes en
  producción», `borrador: false`).
  - **Tesis:** un subagente protege la ventana principal porque devuelve mucho menos de lo que lee (mediana 68 a 1 en
    37 delegaciones reales), pero no ahorra tokens, y un fork no protege el bolsillo porque empieza con toda la
    conversación.
  - **Estructura:** apertura · Qué medí · Lo que salió (tabla) · Lo que no es gratis · Cómo delego ahora · Lo que no
    medí (límites y la comparación controlada de otro autor).
  - **Fuentes:** [documentación de subagentes de Claude Code](https://code.claude.com/docs/en/sub-agents) (contexto
    propio, solo vuelve el resumen, Haiku para controlar costes, el fork hereda la conversación);
    [Pablo Melero, «Delegar no es paralelizar»](https://pablomeleroalonso.me/blog/delegar-no-es-paralelizar/) (57 % más
    de tokens con subagente en su prueba controlada); datos propios.
- Datos propios comprobables: `scripts/medir-subagentes.py` y `docs/blog/datos/subagentes-2026-11.json` (40 filas, del
  29-10 al 28-11-2026; sin rutas, encargos ni contenido).
- Portada `src/assets/blog/lo-que-vuelve-de-un-subagente.webp` (1600×900, dos tintas, sin texto), generada con
  `scripts/portadas/subagente.py` (SVG) y rasterizada con Chrome sin ventana.

## Qué queda fuera

- La calidad de los informes y el coste en euros: la nota los da como no medidos.
- Actualizar la tabla de colores de `docs/blog/PLANTILLA.md` (aún habla de amarillo): cambio aparte.
- Un componente de diagrama para el blog: la nota usa una tabla.
