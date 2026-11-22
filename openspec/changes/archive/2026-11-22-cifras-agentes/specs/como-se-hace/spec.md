## ADDED Requirements

### Requirement: Cifras del trabajo con agentes
La página SHALL incluir una sección «Medido» con las cifras de los PR fusionados de este repositorio en los últimos 90 días: PR fusionados, porcentaje con especificación de OpenSpec, mediana de horas hasta fusionar, mediana de commits tras abrir el PR, revertidos y cerrados sin fusionar. Las cifras MUST calcularse en el build con `scripts/metricas.py` y la API de GitHub, sin contar los bots, y la sección SHALL decir el periodo con sus fechas.

#### Scenario: Tras un merge
- **WHEN** se fusiona un PR y la CI compila la web
- **THEN** la sección «Medido» enseña las cifras recalculadas y el periodo con sus fechas de inicio y fin

#### Scenario: Sin acceso a la API de GitHub
- **WHEN** el cálculo de las cifras falla en la CI
- **THEN** el build no falla, la ejecución deja un aviso y la página enseña las cifras de `src/data/agentes.json` con su fecha

#### Scenario: Una cifra que no se puede medir
- **WHEN** ningún PR tiene revisiones formales en GitHub
- **THEN** la página no enseña «aceptados a la primera» y explica por qué no existe esa cifra

#### Scenario: Móvil
- **WHEN** se ve la sección a 390 px
- **THEN** las cifras van en una columna y no hay desbordamiento horizontal
