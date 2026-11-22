# identidad Specification

## Purpose

Qué paleta, qué contacto y qué datos personales y laborales enseña la web.

## Requirements

### Requirement: Paleta de un solo verde
La web SHALL usar en los dos temas una tinta casi negra o casi blanca, una gama de grises y un único verde de señal.
MUST NOT quedar amarillo en la interfaz, el icono ni la imagen para compartir. Todo el texto MUST cumplir WCAG AA.

#### Scenario: Sin amarillo
- **WHEN** se busca `ffc72c` en `src/`, `public/favicon.svg` y `scripts/og.html`
- **THEN** no aparece

### Requirement: Contacto solo por correo
La portada SHALL ofrecer el correo (enlace y botón de copiar) como única vía de contacto propia. MUST NOT ofrecer un
CV para descargar ni un botón que imprima la página.

#### Scenario: Sin botón de CV
- **WHEN** se abre `/`
- **THEN** no hay ningún botón ni enlace «CV»

### Requirement: Empleador y cifras como en el CV
La web SHALL nombrar a Pangeanic en los puestos desde marzo de 2024 y MUST NOT nombrar sus productos, webs ni
clientes. Las cifras de la portada MUST coincidir con el CV de LinkedIn en español («más de 10 años», 45 M de
pasajeros al año, «6 equipos y más de 15 personas» en Viajando).

#### Scenario: Cifras
- **WHEN** se abre `/`
- **THEN** no aparece «12 años», y el capítulo de Team Leader, la tarjeta de Viajando y la respuesta «¿Ha liderado equipos?» dicen «6 equipos y más de 15 personas»

### Requirement: Titular
El H1 de la portada SHALL ser «Hola, soy Alejandro. Diseño cómo se trabaja con agentes de IA y llevo lo que se
construye a producción.», y la imagen para compartir MUST decir lo mismo. MUST NOT presentar el liderazgo de equipos
como el puesto actual: el liderazgo se cuenta en pasado (Team Leader de Viajando).

#### Scenario: Titular
- **WHEN** se abre `/` a 1440×900
- **THEN** el H1 completo se ve sin hacer scroll

### Requirement: Crédito del diseño fuera del pie
El crédito de la composición SHALL ir en «Cómo se hace» y en el README, con autor, enlace a la obra, licencia
CC BY 4.0 y los cambios hechos. El pie de las páginas MUST NOT llevarlo.

#### Scenario: Crédito
- **WHEN** se abre `/como-se-hace/`
- **THEN** al final aparece el crédito con el enlace a la obra y a la licencia, y el pie de `/` no lo lleva

### Requirement: Trayectoria con FTChart
La trayectoria SHALL tener 7 capítulos en orden cronológico por fecha de inicio, con FTChart como capítulo propio
(«Consultor de IA y desarrollador full-stack», jun 2025 → jun 2026) entre los dos de Pangeanic, más «Las tres capas, a la vez». Sin JavaScript
MUST verse los 8 bloques.

#### Scenario: Etiqueta y orden
- **WHEN** se abre `/` a 1440×900
- **THEN** la etiqueta dice «Capítulo 01 / 08» y los capítulos empiezan en 2009, 2014, 2021, 2022, 2024, 2025 y 2026

### Requirement: Datos del despliegue sin Actions
Mientras un build no salga de una ejecución de GitHub Actions, «Cómo se hace» SHALL decirlo con texto («Ninguna:
desplegado a mano» y «Sin ejecuciones todavía») y MUST NOT mostrar la insignia del workflow.

#### Scenario: Despliegue a mano
- **WHEN** se compila sin `PUBLIC_RUN_URL`
- **THEN** la página no tiene ninguna imagen rota y no enlaza a `badge.svg`

### Requirement: Disponibilidad y fechas como en el CV
La píldora de la foto SHALL decir lo mismo que el estado de la portada («Abierto a conversaciones») y MUST NOT
decir «Disponible». El capítulo de ingeniero independiente SHALL acabar en ene 2024, como en el CV.

#### Scenario: Píldora y capítulo 2022
- **WHEN** se abre `/`
- **THEN** la página no contiene «Disponible», la píldora de la foto dice «Abierto a conversaciones» y el capítulo de 2022 dice «mar 2022 → ene 2024»

### Requirement: Hoy, antes y lo que busca, como en LinkedIn y el CV
La web SHALL dar el puesto actual como en el CV y en LinkedIn («Machine Learning Developer» en Pangeanic, que
también hace de arquitecto de IA y de software), el liderazgo como experiencia pasada y lo que busca al final («un rol
de Arquitecto de IA o Tech Lead»). MUST NOT aparecer «Developer Machine Learning».

#### Scenario: Puesto y búsqueda
- **WHEN** se abre `/`
- **THEN** el capítulo de 2026 dice «Machine Learning Developer», el último bloque de la trayectoria dice «Arquitecto de IA o Tech Lead» y la página no contiene «Developer Machine Learning» ni «Lidero equipos»

### Requirement: Imagen para compartir con versión
La URL de `og:image` y la `image` del JSON-LD SHALL llevar una versión que dependa del contenido de `public/og.png`,
para que las redes vuelvan a descargarla cuando cambie. Con la misma imagen, la URL MUST ser la misma en cada build.

#### Scenario: Versión por contenido
- **WHEN** se compila la web
- **THEN** `og:image` es `https://alejandroduenasreal.me/og.png?v=` seguido de los 8 primeros caracteres hexadecimales del SHA-256 de `public/og.png`, y la `image` del JSON-LD es la misma URL

### Requirement: Iconos para los buscadores
Todas las páginas SHALL declarar el icono «AD» en ICO (con 48 px), en SVG y en PNG cuadrado de 192 px. `/favicon.ico`
MUST responder 200, para los rastreadores que lo buscan ahí por defecto.

#### Scenario: Iconos declarados y servidos
- **WHEN** se abre `/`
- **THEN** el `<head>` lleva `rel="icon"` hacia `/favicon.ico`, `/favicon.svg` y `/favicon-192.png`, y las tres URL responden 200
