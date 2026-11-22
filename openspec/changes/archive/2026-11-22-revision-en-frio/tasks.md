## 1. Reglas

- [x] 1.1 `AGENTS.md`, pasos 6 y 7: revisión y merge en otra sesión, excepción de los arreglos urgentes y archivo de OpenSpec como último commit del mismo PR (se comprueba leyendo el diff)
- [x] 1.2 `openspec/config.yaml`, sección Git: las mismas dos reglas (se comprueba con `openspec validate --all --strict`)

## 2. Página

- [x] 2.1 «Cómo se hace», paso «Publicar»: Alejandro fusiona en otra sesión, nunca en la que se abrió el PR (se comprueba en la vista previa)
- [x] 2.2 «Medido»: una frase que explica por qué la mediana tardará en reflejar la regla (se comprueba en la vista previa)

## 3. Comprobación

- [x] 3.1 `npm run check`, `npm run build` y `openspec validate --all --strict` en verde
- [x] 3.2 Este mismo PR se archiva con su último commit y no se fusiona en la sesión en que se abre
