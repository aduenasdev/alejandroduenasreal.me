## Por qué

«Cómo se hace» enseña el circuito (especificación, agentes, CI, merge), pero no lo mide. La web dice «especificar, comprobar, desplegar con vuelta atrás y medir», y la medida falta. Las cifras del propio repositorio, calculadas en cada build, convierten el circuito en una prueba comprobable por cualquiera.

## Qué cambia

- **Sección nueva «Medido»** en «Cómo se hace», detrás de las comprobaciones. Recoge los PR fusionados de este repositorio en los últimos 90 días:
  - cuántos se fusionaron;
  - qué parte trae especificación de OpenSpec;
  - la mediana de horas hasta fusionar;
  - la mediana de commits de corrección tras abrir el PR;
  - los revertidos y los cerrados sin fusionar.
- **`scripts/metricas.py`:** copia del script de métricas del kit agentes-con-control (MIT, del mismo autor). Calcula las cifras con la API de GitHub y deja fuera los bots.
- **La CI** (`ci-cd.yml`) calcula las cifras antes del build con el token de la propia ejecución. Si falla, deja un aviso y se publica la última foto guardada (`src/data/agentes.json`). El build no falla por eso.
- **Las cifras solo cambian al fusionar:** no hay ejecución programada, para que el merge siga siendo la aprobación de publicar.
- **Regla de contenido** (`AGENTS.md` y `openspec/config.yaml`): además de las cifras del CV, se permiten las que se calculan en el build a partir de datos públicos de este repositorio.

## Qué queda fuera

- **«Aceptados a la primera»:** no existe aquí, porque se revisa y se fusiona sin «Aprobar» formal en GitHub. La página lo explica en vez de inventar la cifra.
- **Métricas de otros repositorios.**
- **Un enlace al kit agentes-con-control:** irá cuando sea público.
