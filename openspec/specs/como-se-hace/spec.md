# como-se-hace Specification

## Purpose

Demostrar con datos reales cómo se especifica, comprueba y despliega la propia web, y quién decide en cada paso.

## Requirements

### Requirement: Datos del despliegue
La página SHALL mostrar el commit corto (enlazado a GitHub), la fecha del build, el enlace a la ejecución de Actions y
la insignia de estado del workflow. En un build local SHALL mostrar «local».

#### Scenario: Tras un merge
- **WHEN** se fusiona un PR y termina el despliegue
- **THEN** la página muestra el hash corto de ese merge, enlazado a su commit

#### Scenario: Build local
- **WHEN** se compila sin `PUBLIC_COMMIT`
- **THEN** el commit y la ejecución muestran «local»

### Requirement: Circuito
La página SHALL incluir un diagrama propio (HTML y CSS, sin imágenes) de Alejandro → agentes → repositorio → PR → CI →
vista previa → merge → producción, horizontal en escritorio y vertical en móvil, sin desbordamiento.

#### Scenario: Móvil
- **WHEN** se ve a 390 px
- **THEN** el circuito va en vertical y no hay desbordamiento horizontal

### Requirement: Workflow real
La página SHALL mostrar el contenido de `.github/workflows/ci-cd.yml` leído en el build, de forma que nunca se
desincronice del fichero.

#### Scenario: Cambia el workflow
- **WHEN** un PR modifica `ci-cd.yml`
- **THEN** la vista previa de ese PR ya enseña el fichero nuevo, sin tocar la página

### Requirement: Quién decide
La página SHALL explicar los cuatro pasos (proponer, construir, comprobar, publicar), qué hace el agente y qué decide
Alejandro, y que el agente nunca fusiona.

#### Scenario: Leer los pasos
- **WHEN** se lee «Cuatro pasos, y quién decide en cada uno»
- **THEN** cada paso tiene una columna «El agente» y otra «Yo», y el paso «Publicar» dice que el agente nunca fusiona

### Requirement: Comprobaciones, vuelta atrás, notas del blog y coste
La página SHALL incluir la tabla de comprobaciones de cada PR, la vuelta atrás en dos niveles, el ciclo de una nota del
blog con sus reglas y el coste («0 €, más el dominio»).

#### Scenario: Recorrer la página
- **WHEN** se recorre la página de arriba abajo
- **THEN** aparecen la tabla de 4 comprobaciones, el revert y el rollback, los 4 pasos de una nota y el coste

### Requirement: Enlazada
La página SHALL enlazarse desde el menú, el pie de todas las páginas y la pregunta sobre despliegue de la portada.

#### Scenario: Desde la portada
- **WHEN** se abre la portada
- **THEN** el menú, el pie y la respuesta «¿Sabe desplegar y operar lo que construye?» enlazan a `/como-se-hace/`
