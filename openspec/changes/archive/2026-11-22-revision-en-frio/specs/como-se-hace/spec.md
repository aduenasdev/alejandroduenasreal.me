## MODIFIED Requirements

### Requirement: Quién decide
La página SHALL explicar los cuatro pasos (proponer, construir, comprobar, publicar), qué hace el agente y qué decide
Alejandro, que el agente nunca fusiona y que Alejandro fusiona en otra sesión, nunca en la misma en que se abrió el PR.

#### Scenario: Leer los pasos
- **WHEN** se lee «Cuatro pasos, y quién decide en cada uno»
- **THEN** cada paso tiene una columna «El agente» y otra «Yo», y el paso «Publicar» dice que el agente nunca fusiona

#### Scenario: Revisión en frío
- **WHEN** se lee la columna «Yo» del paso «Publicar»
- **THEN** dice que Alejandro fusiona en otra sesión, nunca en la misma en que se abrió el PR
