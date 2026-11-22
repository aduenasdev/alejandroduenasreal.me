# Plantilla de nota

Cada nota es **un fichero en español**: `src/content/blog/AAAA-MM-DD-<slug>.md`. El blog no tiene otros idiomas.

La portada (opcional) va en `src/assets/blog/<slug>.webp` (1600×900, ilustración risográfica de dos tintas, sin texto)
y se referencia con una ruta relativa en `portada`. Sin portada, la tarjeta muestra la trama del color del tipo.

```markdown
---
titulo: …                     # ≤ 90 caracteres
descripcion: …                # ≤ 160 caracteres
fecha: 2026-12-07             # el día en que se publica
slug: …                       # la URL /blog/<slug>/: [a-z0-9-], sin repetir
tipo: guia                    # guia | opinion | analisis | caso
serie: Agentes en producción  # opcional
portada: ../../assets/blog/<slug>.webp   # opcional
portadaAlt: …                 # obligatorio si hay portada
etiquetas: [ … ]
borrador: true                # se publica al pasarlo a false (o quitarlo)
---
```

## Reglas

1. **Al menos una nota por semana, sin tope.** Si hay dos listas, se publican las dos. El build solo falla si dos notas
   comparten `slug`.
2. **Cifras con fuente.** Cada nota lleva al menos una cifra con su fuente enlazada y un diagrama o una tabla. Lo que no
   se puede medir se dice como opinión.
3. **Nada de datos de clientes ni de empresas** (ver las reglas de contenido en `AGENTS.md`).
4. **Cada nota es un cambio de OpenSpec** (`skip_specs: true`): la propuesta lleva la tesis, la estructura y las
   fuentes; Alejandro aprueba el alcance y publica con su merge.

## Colores de tipo

| Tipo | Color | Portada |
|---|---|---|
| Guía | verde (`ia`) | tinta verde + amarillo |
| Opinión | amarillo (`senal`) | solo amarillo y negro |
| Análisis | azul (`prod`) | tinta azul + amarillo |
| Caso | rojo (`lid`) | tinta roja + amarillo |
