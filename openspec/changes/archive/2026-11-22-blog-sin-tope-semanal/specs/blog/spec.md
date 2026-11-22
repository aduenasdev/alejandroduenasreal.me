## REMOVED Requirements

### Requirement: Una nota por semana
**Reason**: El tope de una nota por semana ISO obligaba a retrasar notas ya listas y revisadas.
**Migration**: La comprobación de slugs repetidos pasa al requisito «Slugs únicos». Ya no hay comprobación por semana.

## ADDED Requirements

### Requirement: Slugs únicos
El build MUST fallar si dos notas publicadas comparten `slug`. Varias notas MAY publicarse en la misma semana ISO.

#### Scenario: Slug repetido
- **WHEN** dos notas publicadas tienen el mismo `slug`
- **THEN** `npm run build` falla diciendo qué slug está repetido

#### Scenario: Dos notas la misma semana
- **WHEN** hay dos notas publicadas con fechas 2026-12-07 y 2026-12-09 y slugs distintos
- **THEN** `npm run build` termina bien y publica las dos
