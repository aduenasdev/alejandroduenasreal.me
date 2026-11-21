// @ts-check
import { defineConfig, fontProviders } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://alejandroduenasreal.me',
  // Toda la web en español
  i18n: { locales: ['es'], defaultLocale: 'es' },
  // Fuentes servidas desde el propio dominio, con respaldo ajustado para que el texto no salte al cargar
  fonts: [
    { provider: fontProviders.google(), name: 'Sora', cssVariable: '--font-titular', weights: [400, 600, 700], subsets: ['latin'] },
    { provider: fontProviders.google(), name: 'Atkinson Hyperlegible Next', cssVariable: '--font-texto', weights: [400, 600, 700], styles: ['normal', 'italic'], subsets: ['latin'] },
  ],
  vite: { plugins: [tailwindcss()] },
});
