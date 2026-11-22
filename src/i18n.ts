// La web entera, blog incluido, está en español.

/** Ruta del índice del blog. */
export const rutaBlog = '/blog/';

/** Textos de la interfaz del blog. */
export const textos = {
  locale: 'es-ES',
  notas: 'Notas',
  tituloBlog: 'Notas de ingeniería',
  descripcionBlog:
    'Al menos una nota por semana sobre IA en producción, agentes de código y cómo trabajar con ellos sin perder el control.',
  publicado: 'Publicado el',
  minutos: 'min de lectura',
  leer: 'Leer nota →',
  todas: '← Todas las notas',
  teHaServido: '¿Te ha servido?',
  hablemos: 'Hablemos →',
  siguiente: 'Siguiente',
  anterior: 'Anterior',
  sinNotas: 'Todavía no hay notas publicadas. La primera llega pronto.',
  tipos: { guia: 'Guía', opinion: 'Opinión', analisis: 'Análisis', caso: 'Caso' },
  rss: 'RSS de las notas',
} as const;
