// RSS 2.0 del blog, sin dependencias.
import { publicadas, urlEntrada } from './blog';
import { rutaBlog, textos } from './i18n';
import { perfil } from './data/perfil';

const escapa = (s: string) =>
  s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&apos;');

export const rss = async (site: URL) => {
  const notas = await publicadas();
  const enlace = new URL(rutaBlog, site).href;
  const items = notas
    .map((e) => {
      const url = new URL(urlEntrada(e), site).href;
      return `    <item>
      <title>${escapa(e.data.titulo)}</title>
      <link>${url}</link>
      <guid isPermaLink="true">${url}</guid>
      <description>${escapa(e.data.descripcion)}</description>
      <pubDate>${e.data.fecha.toUTCString()}</pubDate>
${e.data.etiquetas.map((c) => `      <category>${escapa(c)}</category>`).join('\n')}
    </item>`;
    })
    .join('\n');
  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>${escapa(`${textos.tituloBlog} · ${perfil.nombre}`)}</title>
    <link>${enlace}</link>
    <atom:link href="${new URL('rss.xml', enlace).href}" rel="self" type="application/rss+xml" />
    <description>${escapa(textos.descripcionBlog)}</description>
    <language>es</language>
${notas[0] ? `    <lastBuildDate>${notas[0].data.fecha.toUTCString()}</lastBuildDate>\n` : ''}${items}
  </channel>
</rss>
`;
  return new Response(xml, { headers: { 'Content-Type': 'application/rss+xml; charset=utf-8' } });
};
