// Sitemap del sitio. Comprueba las reglas del blog en cada build.
import type { APIRoute } from 'astro';
import { comprobarReglas, urlEntrada } from '../blog';
import { rutaBlog } from '../i18n';

export const GET: APIRoute = async ({ site }) => {
  const notas = await comprobarReglas();
  const abs = (p: string) => new URL(p, site).href;
  const dia = (d: Date) => d.toISOString().slice(0, 10);
  const hoy = dia(new Date());
  const urls: { loc: string; lastmod: string }[] = [{ loc: abs('/'), lastmod: hoy }];
  // El índice del blog solo se indexa si hay alguna nota publicada
  if (notas.length) urls.push({ loc: abs(rutaBlog), lastmod: dia(notas[0].data.fecha) });
  for (const e of notas) urls.push({ loc: abs(urlEntrada(e)), lastmod: dia(e.data.fecha) });
  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map((u) => `  <url>\n    <loc>${u.loc}</loc>\n    <lastmod>${u.lastmod}</lastmod>\n  </url>`).join('\n')}
</urlset>
`;
  return new Response(xml, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
};
