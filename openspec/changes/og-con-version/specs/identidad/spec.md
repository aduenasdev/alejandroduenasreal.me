## ADDED Requirements

### Requirement: Imagen para compartir con versión
La URL de `og:image` y la `image` del JSON-LD SHALL llevar una versión que dependa del contenido de `public/og.png`,
para que las redes vuelvan a descargarla cuando cambie. Con la misma imagen, la URL MUST ser la misma en cada build.

#### Scenario: Versión por contenido
- **WHEN** se compila la web
- **THEN** `og:image` es `https://alejandroduenasreal.me/og.png?v=` seguido de los 8 primeros caracteres hexadecimales del SHA-256 de `public/og.png`, y la `image` del JSON-LD es la misma URL
