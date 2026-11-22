## 1. Build

- [x] 1.1 `comprobarReglas` en `src/blog.ts` solo comprueba los slugs; `semanaIso` desaparece (se comprueba con un build que tiene dos notas la misma semana, en una copia de prueba que no se commitea)

## 2. Spec y reglas

- [x] 2.1 Spec `blog`: «Una nota por semana» se sustituye por «Slugs únicos»; propósito al día (se comprueba con `openspec validate --all --strict`)
- [x] 2.2 `docs/blog/PLANTILLA.md`, `AGENTS.md` y `openspec/config.yaml` sin la regla de una por semana (se comprueba leyendo el diff)

## 3. Textos

- [x] 3.1 Subtítulo del blog (`src/i18n.ts`), sección «Notas» de la portada y «Cómo se hace» (se comprueba en la vista previa)
- [x] 3.2 Nota «Hola, soy Alejandro»: primera regla y párrafo de cada semana, sin tocar la descripción ni «Qué busco» (se comprueba en la vista previa)

## 4. Comprobación

- [x] 4.1 `npm run check`, `npm run build` y `openspec validate --all --strict` en verde
- [x] 4.2 El cambio se archiva en el último commit de este PR
