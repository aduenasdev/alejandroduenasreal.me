## Por qué

«Medido» enseña que 12 de los 20 PR fusionados entraron menos de 10 minutos después de abrirse; la mediana es de 0,1 h.
Uno de 549 líneas entró en 8 minutos. Una revisión que encuentra fallos va a unas 400-500 líneas por hora, así que eso
fue un visto bueno, no una revisión. La web dice «revisión humana, obligatoria»: tiene que notarse en sus cifras.

También hay PR que no aportan nada que revisar: 5 de los 20 solo archivan el cambio de OpenSpec después de fusionar.
Inflan la cuenta de PR y bajan la mediana.

## Qué cambia

- **Revisión en frío:** ningún PR se fusiona en la misma sesión en que se abre. Alejandro lo revisa después, en la
  vista previa y con el diff delante, y lo fusiona él. Solo un arreglo urgente de producción, con «urgente» en el
  título, puede fusionarse en la misma sesión.
- **El archivo de OpenSpec va en el mismo PR:** el último commit antes de abrirlo es `openspec archive <id> --yes`,
  y las specs pasan a `openspec/specs/` al fusionar. Ya no hay PR aparte para archivar.
- **Reglas** en `AGENTS.md` (pasos 6 y 7) y en `openspec/config.yaml` (Git).
- **«Cómo se hace»:**
  - el paso «Publicar» dice que Alejandro fusiona en otra sesión;
  - la sección «Medido» explica que los PR anteriores, fusionados en minutos, pesan en la mediana hasta que salgan de
    la ventana de 90 días.

## Qué queda fuera

- **Cambiar el cálculo de las cifras:** no se excluye ningún PR ni se espera a propósito. La mediana cambia porque
  cambia la forma de revisar.
- **Una métrica de velocidad de revisión** (líneas por hora): es una idea para el script del kit, no para este cambio.
- **Los PR ya fusionados:** se quedan como están.
