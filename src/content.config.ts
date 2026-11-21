import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  // Los ficheros que empiezan por «_» no se publican
  loader: glob({ base: './src/content/blog', pattern: '**/[^_]*.md' }),
  schema: ({ image }) =>
    z.object({
      titulo: z.string().max(90),
      descripcion: z.string().max(160),
      fecha: z.coerce.date(),
      slug: z.string().regex(/^[a-z0-9-]+$/), // la URL: /blog/<slug>/
      tipo: z.enum(['guia', 'opinion', 'analisis', 'caso']).default('opinion'),
      serie: z.string().optional(), // p. ej. «Agentes en producción»
      portada: image().optional(), // ilustración risográfica
      portadaAlt: z.string().optional(),
      etiquetas: z.array(z.string()).default([]),
      borrador: z.boolean().default(false),
    }),
});

export const collections = { blog };
