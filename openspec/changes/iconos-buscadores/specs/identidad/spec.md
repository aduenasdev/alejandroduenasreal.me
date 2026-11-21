## ADDED Requirements

### Requirement: Iconos para los buscadores
Todas las páginas SHALL declarar el icono «AD» en ICO (con 48 px), en SVG y en PNG cuadrado de 192 px. `/favicon.ico`
MUST responder 200, para los rastreadores que lo buscan ahí por defecto.

#### Scenario: Iconos declarados y servidos
- **WHEN** se abre `/`
- **THEN** el `<head>` lleva `rel="icon"` hacia `/favicon.ico`, `/favicon.svg` y `/favicon-192.png`, y las tres URL responden 200
