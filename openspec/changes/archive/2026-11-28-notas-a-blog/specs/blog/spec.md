## ADDED Requirements

### Requirement: Ruta /notas
El sitio SHALL redirigir con 301 `/notas` y `/notas/` a `/blog/`, y no SHALL redirigir ninguna otra ruta bajo `/notas/`.

#### Scenario: Alguien escribe /notas
- **WHEN** se pide `https://alejandroduenasreal.me/notas` o `https://alejandroduenasreal.me/notas/`
- **THEN** la respuesta es un 301 con `Location: /blog/`, y `/blog/` responde 200

#### Scenario: Una nota que no existe bajo /notas
- **WHEN** se pide `https://alejandroduenasreal.me/notas/cualquier-cosa`
- **THEN** la respuesta es la página 404
