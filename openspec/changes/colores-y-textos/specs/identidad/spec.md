# Spec Delta

## Purpose

Qué paleta, qué contacto y qué datos personales y laborales enseña la web.

## ADDED Requirements

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
pasajeros al año); el número de equipos liderados solo aparece en la nota del blog.

#### Scenario: Cifras
- **WHEN** se busca «12 años» o «6 equipos» en `src/data/perfil.ts`
- **THEN** no aparece

### Requirement: Titular de liderazgo
El H1 de la portada SHALL ser «Hola, soy Alejandro. Lidero equipos que desarrollan con agentes de IA y llevo lo que
construyen a producción.», y la imagen para compartir MUST decir lo mismo.

#### Scenario: Titular
- **WHEN** se abre `/` a 1440×900
- **THEN** el H1 completo se ve sin hacer scroll
