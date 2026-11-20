// @ts-check
import { defineConfig, fontProviders } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://alejandroduenasreal.me',
  // Español en la raíz y el inglés bajo /en/: cada idioma con su URL, indexables los dos
  i18n: { locales: ['es', 'en'], defaultLocale: 'es', routing: { prefixDefaultLocale: false } },
  // Fuentes servidas desde el propio dominio, con respaldo ajustado para que el texto no salte al cargar
  fonts: [
    { provider: fontProviders.google(), name: 'Sora', cssVariable: '--font-titular', weights: [400, 600, 700], subsets: ['latin'] },
    { provider: fontProviders.google(), name: 'Atkinson Hyperlegible Next', cssVariable: '--font-texto', weights: [400, 600, 700], styles: ['normal', 'italic'], subsets: ['latin'] },
  ],
  vite: { plugins: [tailwindcss()] },
});
