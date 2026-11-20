export type Idioma = 'es' | 'en';
export const idiomas: Idioma[] = ['es', 'en'];

/** Ruta del índice del blog de cada idioma (el español va en la raíz). */
export const rutaBlog = (lang: Idioma) => (lang === 'es' ? '/blog/' : '/en/blog/');

/** Textos de la interfaz que cambian con el idioma. */
export const textos = {
  es: {
    locale: 'es-ES',
    notas: 'Notas',
    tituloBlog: 'Notas de ingeniería',
    descripcionBlog:
      'Una nota por semana sobre IA en producción, agentes de código y cómo trabajar con ellos sin perder el control.',
    publicado: 'Publicado el',
    minutos: 'min de lectura',
    leer: 'Leer nota →',
    todas: '← Todas las notas',
    otraVersion: 'Read in English',
    teHaServido: '¿Te ha servido?',
    hablemos: 'Hablemos →',
    siguiente: 'Siguiente',
    anterior: 'Anterior',
    sinNotas: 'Todavía no hay notas publicadas. La primera llega pronto.',
    tipos: { guia: 'Guía', opinion: 'Opinión', analisis: 'Análisis', caso: 'Caso' },
    rss: 'RSS de las notas',
  },
  en: {
    locale: 'en-GB',
    notas: 'Notes',
    tituloBlog: 'Engineering notes',
    descripcionBlog:
      'One note a week about AI in production, coding agents and how to work with them without losing control.',
    publicado: 'Published on',
    minutos: 'min read',
    leer: 'Read note →',
    todas: '← All notes',
    otraVersion: 'Leer en español',
    teHaServido: 'Was this useful?',
    hablemos: "Let's talk →",
    siguiente: 'Next',
    anterior: 'Previous',
    sinNotas: 'No notes published yet. The first one is coming soon.',
    tipos: { guia: 'Guide', opinion: 'Opinion', analisis: 'Analysis', caso: 'Case' },
    rss: 'Notes RSS feed',
  },
} as const;
