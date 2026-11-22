// Todo el texto de la web sale de aquí. Los componentes no llevan texto propio
// salvo los encabezados de sección. Solo hechos comprobables (ver AGENTS.md).

export const perfil = {
  nombre: 'Alejandro Dueñas Real',
  nombreCorto: 'Alejandro Dueñas',
  rol: 'Agentes de IA en producción y LLMOps',                       // <title> y og:image:alt
  titulo: 'Machine Learning Developer · Arquitecto de IA y de Software', // jobTitle del JSON-LD (el del CV)
  ubicacion: 'España · remoto o híbrido',
  estado: 'Abierto a conversaciones',
  correo: 'aduenasdev@gmail.com',
  linkedin: 'https://www.linkedin.com/in/aduenasdev',
  github: 'https://github.com/aduenasdev',
  sitio: 'https://alejandroduenasreal.me',
};

// Meta description (≤ 160)
export const descripcion =
  'Machine Learning Developer en Pangeanic, también arquitecto de IA y de software: agentes de IA en producción con revisión, pruebas y evaluación.';

// Crédito que exige la licencia CC BY 4.0 de Figma Community: autor, enlace, licencia y cambios. Va en «Cómo se hace».
export const atribucion = {
  obra: '«Graphic Designer Portfolio Homepage»',
  autor: 'Can Aydın',
  url: 'https://www.figma.com/community/file/1325338426202374850',
  licencia: 'CC BY 4.0',
  licenciaUrl: 'https://creativecommons.org/licenses/by/4.0/deed.es',
  cambios: 'Adaptada: colores, textos y componentes propios.',
};

// knowsAbout del JSON-LD
export const conocimientos = [
  'Inteligencia artificial generativa', 'LLM en producción', 'Agentes de IA', 'Model Context Protocol (MCP)',
  'Evaluación de modelos', 'Liderazgo de equipos de ingeniería', 'Ingeniería de plataforma',
  'Procesamiento del lenguaje natural', 'Desarrollo full-stack', 'LLMOps', 'MLOps', 'Observabilidad de LLM',
  'Kubernetes', 'Terraform', 'CI/CD', 'Python', 'Java', 'AWS',
];

export const portada = {
  saludo: 'Hola, soy',
  nombre: 'Alejandro.',
  lineasTitular: ['Diseño cómo se trabaja con agentes de IA y llevo lo que se construye a producción.'],
  insignia: 'LLMOps y plataforma',
  entrada:
    'Diseño cómo se trabaja con agentes de IA sin perder el control: cada cambio, lo escriba una persona o un agente, pasa por revisión, pruebas y evaluación antes de salir, y siempre hay vuelta atrás. Más de 10 años construyendo software; hoy Machine Learning Developer en Pangeanic, donde también hago de arquitecto de IA y de software, y antes Team Leader de 6 equipos y más de 15 personas en una plataforma nacional con más de 45 M de pasajeros al año.',
  cintaUno: ['Agentes en producción', 'LLMOps', 'Evaluación', 'Observabilidad', 'Guardrails', 'Coste por petición', 'MCP', 'RAG'],
  cintaDos: ['AWS Bedrock', 'Azure OpenAI', 'Vertex AI', 'Kubernetes', 'Terraform', 'Docker', 'CI/CD', 'Python', 'LangGraph', 'Next.js'],
};

export type Capa = 'producto' | 'liderazgo' | 'ia';
export const capas: Record<Capa, string> = { producto: 'Producto', liderazgo: 'Liderazgo', ia: 'IA' };

export const servicios: { titulo: string; texto: string; capa: Capa | 'senal' }[] = [
  { titulo: 'Arquitectura de agentes', texto: 'Arquitectura de agentes y LLM: RAG con búsqueda híbrida (semántica, BM25 y metadatos), herramientas y servidores MCP, con permisos y límites claros de lo que puede hacer cada uno.', capa: 'ia' },
  { titulo: 'Despliegue y plataforma', texto: 'CI/CD, Docker, Kubernetes y Terraform en AWS: imágenes inmutables, despliegues sin corte y vuelta atrás preparada.', capa: 'producto' },
  { titulo: 'Observabilidad, evaluación y coste', texto: 'Trazas de cada llamada, un banco de evaluación antes de cada cambio, guardrails con nombre (cita obligatoria, modelo que falla en cerrado, revisión humana) y el coste de modelos e infraestructura bajo control.', capa: 'senal' },
  { titulo: 'Producto y equipo', texto: 'Full-stack con diseño y frontend propios (Next.js, Python, Java, .NET) y experiencia como Team Leader de 6 equipos y más de 15 personas.', capa: 'liderazgo' },
];

// Capítulos en orden cronológico. `capas`: cualitativo (encendida/apagada). Fechas y puestos como en el CV.
export const capitulos: { ano: string; fecha: string; puesto: string; donde: string; texto: string; capas: Capa[]; suma: string[] }[] = [
  { ano: '2009', fecha: '2009 → 2014', puesto: 'Licenciatura en Ciencias de la Computación', donde: 'Universidad Central «Marta Abreu» de Las Villas', texto: 'Algoritmos, redes, bases de datos e ingeniería de software.', capas: [], suma: ['La base'] },
  { ano: '2014', fecha: 'sep 2014 → feb 2021', puesto: 'Desarrollador full-stack y móvil', donde: 'SITRANS', texto: 'App Android de Viajando (Java → Kotlin) y su plataforma web; ciclo completo, del análisis al despliegue.', capas: ['producto'], suma: ['+ Producto full-stack y móvil'] },
  { ano: '2021', fecha: 'feb 2021 → ene 2024', puesto: 'Team Leader', donde: 'SITRANS · Viajando', texto: 'Al frente de 6 equipos y más de 15 personas (desarrollo, QA, soporte e infraestructura) en la plataforma nacional de pasajes: arquitectura y dirección técnica, entregas, pagos y antifraude, en coordinación con el operador y el ministerio.', capas: ['producto', 'liderazgo'], suma: ['+ Liderazgo de 6 equipos', '45 M de pasajeros al año'] },
  { ano: '2022', fecha: 'mar 2022 → ene 2024', puesto: 'Ingeniero y consultor independiente', donde: 'Clientes de EE. UU., México y Panamá', texto: 'Logística para la Zona Libre de Colón (Spring Boot, Next.js, AWS), un SaaS de viajes con más de 86.000 hoteles y un SaaS sobre WordPress para una constructora de EE. UU., con plugins propios para pagos e integraciones y la infraestructura a mi cargo. Preventa, propuestas y PoC.', capas: ['producto'], suma: ['+ Preventa, PoC y DevOps'] },
  { ano: '2024', fecha: 'mar 2024 → abr 2026', puesto: 'Desarrollador de aplicaciones', donde: 'Pangeanic · externo, remoto', texto: 'Entré para hacerme cargo de servicios en producción: mantener, ampliar y dar soporte a los servicios en Java/Spring Boot, construir APIs nuevas en Java y Next.js, y desarrollar la web en Next.js y React. Migré APIs de Java 8 a Java 21 y de Java a Python, con Docker en AWS, y puse al día la infraestructura y los despliegues.', capas: ['producto', 'ia'], suma: ['+ Migraciones Java 8 → 21 y a Python'] },
  { ano: '2025', fecha: 'jun 2025 → jun 2026', puesto: 'Consultor de IA y desarrollador full-stack', donde: 'FTChart · EE. UU., remoto', texto: 'IA clínica para médicos: un agente RAG que elige entre búsqueda semántica, BM25 y por metadatos; respuestas que citan la página exacta, y guardrails que fallan en cerrado.', capas: ['producto', 'ia'], suma: ['+ Agentes y guardrails en producción'] },
  { ano: '2026', fecha: 'abr 2026 → hoy', puesto: 'Machine Learning Developer', donde: 'Pangeanic · plantilla', texto: 'También arquitecto de IA y de software. LLM, RAG y NLP en producción; modelos con PyTorch en GPU; microservicios en Python, Node.js y Java; interfaces en Next.js; plataforma interna para trabajar con agentes de código.', capas: ['producto', 'ia'], suma: ['+ LLM, RAG y agentes en producción'] },
];
export const proximoCapitulo = {
  puesto: 'Las tres capas, a la vez',
  texto: 'Diseñar y operar agentes de IA en producción, y la plataforma que los sostiene, al frente de un equipo.',
  capas: ['producto', 'liderazgo', 'ia'] as Capa[],
};

export const entrega = {
  intro: 'La IA acelera, pero no decide sola. Cada cambio, lo escriba una persona o un agente, recorre el mismo camino.',
  pasos: [
    { nombre: 'Especificación', detalle: 'qué y por qué' },
    { nombre: 'Agente', detalle: 'con reglas y permisos' },
    { nombre: 'Revisión', detalle: 'humana, obligatoria' },
    { nombre: 'Pruebas', detalle: 'en la CI' },
    { nombre: 'Evaluación', detalle: 'umbral de calidad', control: true },
    { nombre: 'Despliegue', detalle: 'con vuelta atrás' },
  ] as { nombre: string; detalle: string; control?: boolean }[],
  base: 'reglas · permisos · memoria · hooks · servidores MCP · trazas y coste por petición',
  retorno: 'Lo que falla en producción vuelve a la especificación como prueba nueva.',
};

export const trabajos: { sello: string; titulo: string; url?: string; contexto: string; hecho: string; stack: string[]; tinta: 'senal' | 'prod' | 'lid' | 'ia' }[] = [
  { sello: 'Ahora', titulo: 'LLM y agentes en producción', contexto: 'Pangeanic, desde 2024.',
    hecho: 'Integración de LLM en flujos de producción con recuperación de contexto (RAG), trazas de cada llamada y evaluación con un banco fijo antes de cada cambio. Microservicios, interfaces en Next.js, despliegues sin corte en AWS y agentes de código con revisión, pruebas y permisos.',
    stack: ['Python', 'LangChain / LangGraph', 'AWS Bedrock', 'pgvector', 'Next.js'], tinta: 'senal' },
  { sello: 'EE. UU.', titulo: 'FTChart · IA clínica con respuestas verificables', url: 'https://ftchart.com/', contexto: 'Consultor de IA y desarrollador full-stack, de junio de 2025 a junio de 2026. Plataforma para médicos de EE. UU., en producción.',
    hecho: 'Un agente RAG que, para cada pregunta, elige entre búsqueda semántica, por palabras clave (BM25) y por metadatos del historial. Guardrails con nombre: cada afirmación cita la página exacta de la que sale; el modelo lo elige la aplicación y, si ninguno es de confianza, la pregunta no sale; los datos del paciente se tokenizan antes de llegar a un modelo remoto; la salida del modelo se sanea como entrada no fiable, y una persona revisa cada nota de IA antes de archivarla. Más de 7.500 pruebas automáticas antes de cada versión.',
    stack: ['RAG agéntico', 'Búsqueda híbrida', 'Next.js', 'TypeScript', 'Gemini en Vertex AI'], tinta: 'ia' },
  { sello: '2021 → 2024', titulo: 'Viajando · billetes para todo un país', contexto: 'Plataforma oficial de billetes de autobús y tren de Cuba, más de 45 M de pasajeros al año.',
    hecho: 'Como Team Leader de 6 equipos y más de 15 personas: pagos integrados, controles contra la reventa, colas automáticas y la app Android migrada de Java a Kotlin sin parar el servicio.',
    stack: ['Java / Spring Boot', 'Kotlin', 'PHP', 'Python', 'Android'], tinta: 'lid' },
  { sello: 'En equipo', titulo: 'Vaquify · gestión ganadera sin señal', url: 'https://vaquify.com/', contexto: 'Software para fincas ganaderas, en producción.',
    hecho: 'Partos, servicios y ordeño se registran con o sin cobertura, y la aplicación calcula los indicadores del rebaño. Rediseño del frontend para teléfono, tableta y escritorio, y despliegues en producción.',
    stack: ['Next.js', 'Python', 'PostgreSQL', 'Docker'], tinta: 'ia' },
  { sello: 'Proyecto propio', titulo: 'soberquant', url: 'https://soberquant.com', contexto: 'Análisis de mercados financieros con agentes.',
    hecho: 'Agentes LLM que leen noticias y estrategias cuantitativas con backtest, con colas de trabajo y su propia interfaz.',
    stack: ['Python', 'PyTorch / XGBoost', 'Celery + Redis', 'PostgreSQL', 'Next.js'], tinta: 'prod' },
];

export const preguntas: { pregunta: string; respuesta: string; fuentes: { texto: string; url: string }[] }[] = [
  { pregunta: '¿Ha liderado equipos?',
    respuesta: 'Sí. De 2021 a 2024 fue Team Leader de Viajando, la plataforma oficial de billetes de autobús y tren de Cuba: 6 equipos y más de 15 personas entre desarrollo, QA, soporte e infraestructura; arquitectura y dirección técnica, entregas, pagos y antifraude, en coordinación con el operador y el ministerio.',
    fuentes: [{ texto: 'LinkedIn · experiencia en SITRANS (2021 → 2024)', url: 'https://www.linkedin.com/in/aduenasdev' }, { texto: 'Trayectoria · Team Leader', url: '#trayectoria' }] },
  { pregunta: '¿Ha llevado IA a producción?',
    respuesta: 'Sí. En Pangeanic, desde 2024, lleva LLM, RAG y NLP a producción con despliegues en AWS y evaluación antes de cada cambio. En FTChart (2025-2026), IA clínica para médicos de EE. UU.: un agente RAG con búsqueda semántica, BM25 y por metadatos, respuestas que citan la página exacta, guardrails que fallan en cerrado y revisión humana antes de archivar nada.',
    fuentes: [{ texto: 'ftchart.com', url: 'https://ftchart.com/' }, { texto: 'LinkedIn · experiencia actual', url: 'https://www.linkedin.com/in/aduenasdev' }] },
  { pregunta: '¿Sabe desplegar y operar lo que construye?',
    respuesta: 'Sí. Esta misma web se especifica con OpenSpec, se comprueba en CI y se despliega sola en Cloudflare Pages con vista previa por PR y vuelta atrás; en su trabajo, CI/CD, Docker, Kubernetes y Terraform en AWS, con trazas, evaluación y control del coste.',
    fuentes: [{ texto: 'Cómo se hace esta web', url: '/como-se-hace/' }, { texto: 'GitHub · el repositorio de esta web', url: 'https://github.com/aduenasdev/alejandroduenasreal.me' }] },
  { pregunta: '¿Diseña y construye el frontend?',
    respuesta: 'Sí, de punta a punta: la web y la aplicación de FTChart, la app Android y la web de Viajando, y esta web. Diseño, componentes, accesibilidad y despliegue.',
    fuentes: [{ texto: 'ftchart.com', url: 'https://ftchart.com/' }, { texto: 'GitHub · aduenasdev', url: 'https://github.com/aduenasdev' }] },
  { pregunta: '¿Qué formación tiene en IA?',
    respuesta: 'Licenciado en Ciencias de la Computación. En 2026: Machine Learning (DeepLearning.AI y Stanford), Google AI y dos especializaciones en agentes de IA. Todas se pueden verificar.',
    fuentes: [{ texto: 'Formación · certificados verificables', url: '#formacion' }, { texto: 'Machine Learning Specialization · Coursera', url: 'https://www.coursera.org/account/accomplishments/specialization/certificate/ZDQEGONHQ0H1' }] },
  { pregunta: '¿Dónde y cómo puede trabajar?',
    respuesta: 'Desde España, en remoto o híbrido. Abierto a conversaciones ahora.',
    fuentes: [{ texto: 'Hablemos · contacto', url: '#hablemos' }] },
];

export const formacion = [
  { titulo: 'Hands-on Agentic AI: Building Intelligent Agents', emisor: 'Coursera · especialización', fecha: 'oct 2026', url: 'https://www.coursera.org/account/accomplishments/specialization/U4HCH6O34MVK' },
  { titulo: 'Autonomous AI Agent Systems and Orchestration', emisor: 'Edureka · Coursera', fecha: 'oct 2026', url: 'https://www.coursera.org/account/accomplishments/specialization/certificate/HMHOSDPRHZU3' },
  { titulo: 'Machine Learning Specialization', emisor: 'DeepLearning.AI y Stanford', fecha: 'sep 2026', url: 'https://www.coursera.org/account/accomplishments/specialization/certificate/ZDQEGONHQ0H1' },
  { titulo: 'Google Project Management', emisor: 'Google · certificado profesional', fecha: 'sep 2026', url: 'https://coursera.org/verify/professional-cert/SBMWF98CNEZD' },
  { titulo: 'Google AI', emisor: 'Google · certificado profesional', fecha: 'ago 2026', url: 'https://coursera.org/verify/professional-cert/WOJC9HBYGM7J' },
];

export const contacto = {
  titulo: '¿Construimos IA que llegue a producción?',
  texto: 'Una conversación de 30 minutos sobre tu equipo y lo que necesita. Escríbeme o copia el correo con un clic.',
};
