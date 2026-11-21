// URL de la imagen para compartir con una versión sacada de su contenido: si `og.png` cambia, cambia la URL y las
// redes (LinkedIn guarda la imagen en caché por su URL) la vuelven a descargar.
import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';

const version = createHash('sha256').update(readFileSync('public/og.png')).digest('hex').slice(0, 8);

export const urlOg = (sitio: string | URL) => `${new URL('/og.png', sitio).href}?v=${version}`;
