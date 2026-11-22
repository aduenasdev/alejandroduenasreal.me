import { getCollection, type CollectionEntry } from 'astro:content';
import { rutaBlog, textos } from './i18n';

export type Entrada = CollectionEntry<'blog'>;
export type Tipo = Entrada['data']['tipo'];

/** Notas publicadas (sin borradores), de la más nueva a la más vieja. */
export const publicadas = async () =>
  (await getCollection('blog', (e) => !e.data.borrador)).sort((a, b) => b.data.fecha.valueOf() - a.data.fecha.valueOf());
export const urlEntrada = (e: Entrada) => `${rutaBlog}${e.data.slug}/`;
export const minutosLectura = (texto = '') => Math.max(1, Math.round(texto.split(/\s+/).filter(Boolean).length / 220));

/** Fecha corta: «lun 23 nov». */
export const fechaCorta = (d: Date) =>
  new Intl.DateTimeFormat(textos.locale, { weekday: 'short', day: 'numeric', month: 'short', timeZone: 'UTC' })
    .format(d)
    .replace(/[,.]/g, '');
/** Fecha larga: «23 de noviembre de 2026». */
export const fechaLarga = (d: Date) =>
  new Intl.DateTimeFormat(textos.locale, { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' }).format(d);

/** Color de cada tipo de nota (solo para formas, nunca para texto). */
export const colorTipo: Record<Tipo, string> = { guia: 'var(--ia)', opinion: 'var(--color-senal)', analisis: 'var(--prod)', caso: 'var(--lid)' };

/** La regla del blog: sin slugs repetidos (si no, el build falla). Puede haber varias notas la misma semana. */
export const comprobarReglas = async () => {
  const todas = await publicadas();
  const slugs = new Set<string>();
  for (const e of todas) {
    if (slugs.has(e.data.slug)) throw new Error(`Blog: el slug «${e.data.slug}» está repetido.`);
    slugs.add(e.data.slug);
  }
  return todas;
};
