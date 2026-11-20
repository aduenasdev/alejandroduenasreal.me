# Spec Delta

## Purpose

La portada presenta a Alejandro a reclutadores y responsables técnicos (quién es, qué hace, cómo ha llegado y cómo
contactarle), con pruebas comprobables y sin contenido que no pueda publicarse.

## ADDED Requirements

### Requirement: Presentación inmediata
La portada SHALL mostrar, sin hacer scroll en escritorio: la etiqueta «Abierto a conversaciones · LLMOps y
plataforma», el H1 «Hola, soy Alejandro. Diseño y opero agentes de IA en producción.», el párrafo de entrada,
«Hablemos», «Ver mi trabajo» y la tarjeta de la foto.

#### Scenario: Escritorio
- **WHEN** se abre a 1440×900
- **THEN** se ven todos esos elementos sin hacer scroll

### Requirement: Orden de secciones
La portada SHALL seguir este orden: Portada, Cintas, Qué hago, Cómo trabajo, Trayectoria, Trabajo, Preguntas,
Formación, Notas (solo si hay publicadas) y Hablemos. Todo el texto MUST salir de `src/data/perfil.ts`.

#### Scenario: Sin notas publicadas
- **WHEN** el blog no tiene notas publicadas
- **THEN** no aparece la sección Notas ni el enlace del menú

### Requirement: Trayectoria por capítulos
La trayectoria SHALL mostrar los capítulos en orden cronológico y terminar en «Las tres capas, a la vez». En
escritorio, una columna fija SHALL mostrar el año, el puesto, el lugar y las tres capas del capítulo central. Las
capas MUST ser cualitativas: encendida o apagada, sin porcentajes.

#### Scenario: Capítulo 4 en el centro
- **WHEN** «Ingeniero de software independiente» queda en el centro
- **THEN** el año muestra 2022, la etiqueta «Capítulo 04 / 07», y producto e IA quedan encendidas y liderazgo apagada

#### Scenario: Último capítulo en el centro
- **WHEN** el último capítulo queda en el centro
- **THEN** la etiqueta dice «Próximo capítulo» y las tres capas quedan encendidas

#### Scenario: Móvil
- **WHEN** se ve a 390 px
- **THEN** cada capítulo lleva su año y sus capas, sin columna fija ni desbordamiento horizontal

### Requirement: Sin JavaScript
Sin JavaScript, la portada SHALL mostrar todo el contenido: los 7 capítulos y todas las respuestas, sin botones que
no funcionen.

#### Scenario: JavaScript desactivado
- **WHEN** se abre la portada con JavaScript desactivado
- **THEN** se ven los 7 capítulos al 100 % y las 6 respuestas, y no aparecen los botones de pregunta

### Requirement: Movimiento reducido
Con `prefers-reduced-motion: reduce`, la portada MUST NOT tener animaciones ni transiciones.

#### Scenario: Preferencia del sistema
- **WHEN** el sistema pide movimiento reducido
- **THEN** las cintas están quietas, el año cambia sin transición y el punto no late

### Requirement: Preguntas con fuente
Cada respuesta SHALL enlazar al menos una fuente. Con JavaScript, se ve una respuesta a la vez y `aria-pressed`
refleja la pregunta elegida.

#### Scenario: Elegir otra pregunta
- **WHEN** se pulsa la pregunta 03
- **THEN** se ve solo su respuesta, su botón tiene `aria-pressed="true"` y los demás `false`

### Requirement: Contacto
La portada SHALL mostrar el correo como enlace `mailto:` visible, «Escríbeme» y «Copiar». «Copiar» copia el correo,
avisa y MUST NOT navegar.

#### Scenario: Copiar el correo
- **WHEN** se pulsa «Copiar»
- **THEN** el correo queda en el portapapeles, aparece «Correo copiado: …» y la URL no cambia

### Requirement: Temas
La portada SHALL abrirse en noche, con un interruptor a día que se recuerda. Todo el texto MUST cumplir WCAG AA en los
dos temas.

#### Scenario: Elegir el día
- **WHEN** se pulsa el interruptor y se recarga la página
- **THEN** la página sigue en día y el botón tiene `aria-pressed="false"`

### Requirement: Retrato opcional
Con `retrato-noche`, `retrato-dia` o `retrato` en `src/assets/`, la foto SHALL mostrarse según el tema. Sin ellos se
muestra el monograma, y el build MUST NOT fallar.

#### Scenario: Sin retratos
- **WHEN** no hay ningún retrato en `src/assets/`
- **THEN** el build termina bien y la ventana redonda muestra el monograma en trama

### Requirement: Impresión
Imprimir la portada SHALL dar un CV en blanco y negro, sin decoración, en 3 páginas A4 como mucho.

#### Scenario: CV en PDF
- **WHEN** se pulsa «CV en PDF» y se imprime en A4
- **THEN** salen 3 páginas como mucho, con el contacto bajo el titular y sin foto, cintas, preguntas ni botones

### Requirement: Contenido publicable
La portada MUST NOT nombrar al empleador actual, sus productos, sus webs o sus clientes, ni inventar puestos ni
poner una ciudad. De los clientes, solo FTChart.

#### Scenario: Revisión del contenido
- **WHEN** Alejandro revisa la vista previa de un PR
- **THEN** la portada no nombra al empleador actual ni a clientes distintos de FTChart, y el puesto actual es el del CV

### Requirement: Atribución
El pie de todas las páginas SHALL llevar la atribución del diseño con su enlace.

#### Scenario: Cualquier página
- **WHEN** se abre cualquier página
- **THEN** el pie enlaza a `https://www.figma.com/community/file/1325338426202374850`

### Requirement: Datos estructurados
La portada SHALL llevar JSON-LD `Person` con nombre, `jobTitle`, URL, imagen, país (`ES`, sin ciudad), `sameAs`
(LinkedIn y GitHub) y `knowsAbout`.

#### Scenario: Validar el JSON-LD
- **WHEN** se lee el `<script type="application/ld+json">` de la portada
- **THEN** es JSON válido de tipo `Person` y `address` solo tiene `addressCountry: "ES"`
