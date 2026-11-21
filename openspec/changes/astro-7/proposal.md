## Por qué

Dependabot abrió dos PR de seguridad (#8: sharp 0.35.5 con astro; #9: astro 7.4.7) y los dos fallan en
`astro check`: Astro 7 usa Vite 8 (`transformWithOxc`), pero `package.json` fija `overrides.vite` en 7.3.8. Las
reglas del repo piden subir Vite solo junto con Astro.

## Qué cambia

- `astro` 6.4.8 → 7.4.7 (trae sharp 0.35.5, el arreglo de seguridad del #8).
- `overrides.vite` 7.3.8 → 8.3.8, la versión que pide Astro 7 (`^8.3.5`); `@tailwindcss/vite` 4.3.5 ya admite Vite 8.
- `engines.node` ≥ 22.23.4, el mínimo de Astro 7. La CI sigue con Node 24 (`.node-version`).
- `AGENTS.md`: la trampa de Vite, al día.

## Qué queda fuera

- Cambios visibles en la web: la portada, el blog y «Cómo se hace» deben verse igual.
- TypeScript 7: `@astrojs/check` 0.9.12 sigue admitiendo solo TypeScript 5 o 6.
