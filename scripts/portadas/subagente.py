"""Portada de «Lo que vuelve de un subagente»: risografía isométrica de dos tintas, hecha con código.

Uso: python scripts/portadas/subagente.py > /tmp/portada.svg
Se rasteriza a 1600×900 con Chrome sin ventana y se pasa a WebP (ver docs/blog/PLANTILLA.md).
"""
import math, random

W, H = 1600, 900
PAPEL, VERDE, GRIS = '#1b1d1c', '#3fcf8e', '#edefee'
S = 40                      # tamaño de una unidad isométrica en px
OX, OY = 740, 500           # origen en pantalla
C, SN = math.cos(math.radians(30)), math.sin(math.radians(30))
random.seed(7)


def p(x, y, z=0):
    return (OX + (x - y) * C * S, OY + (x + y) * SN * S - z * S)


def poly(pts, **a):
    d = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    attrs = ' '.join(f'{k.replace("_", "-")}="{v}"' for k, v in a.items())
    return f'<polygon points="{d}" {attrs}/>'


def caja(x, y, z, dx, dy, dz, arriba, izq, der):
    """Caja isométrica: cara de arriba, la que mira a la izquierda (y+) y la que mira a la derecha (x+)."""
    t = [p(x, y, z + dz), p(x + dx, y, z + dz), p(x + dx, y + dy, z + dz), p(x, y + dy, z + dz)]
    l = [p(x, y + dy, z), p(x + dx, y + dy, z), p(x + dx, y + dy, z + dz), p(x, y + dy, z + dz)]
    r = [p(x + dx, y, z), p(x + dx, y + dy, z), p(x + dx, y + dy, z + dz), p(x + dx, y, z + dz)]
    return poly(l, **izq) + poly(r, **der) + poly(t, **arriba)


out = []
# Suelo: una rejilla de puntos muy suave
for i in range(-14, 16):
    for j in range(-14, 16):
        x, y = p(i, j)
        if 0 < x < W and 0 < y < H:
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.6" fill="{GRIS}" opacity=".14"/>')

# Archivo: estanterías altas al fondo a la derecha, llenas de papeles
lleno = dict(fill=VERDE)
trama = dict(fill='url(#trama-verde)')
gris_t = dict(fill='url(#trama-gris)')
linea = dict(fill='none', stroke=GRIS, stroke_width='2')
for fila in range(3):
    for col in range(4):
        x, y = 2 + col * 2.2, -9 + fila * 2.6
        alto = random.choice([4, 5, 5, 6])
        out.append(caja(x, y, 0, 1.6, 1.2, alto, arriba=lleno, izq=trama, der=gris_t))
        for k in range(1, alto * 2):           # baldas con legajos (cara izquierda)
            z = k * 0.5
            a, b = p(x + 0.1, y + 1.2, z), p(x + 1.5, y + 1.2, z)
            out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{PAPEL}" stroke-width="2.4"/>')
# Pilas de papeles sueltos delante del archivo
for (x, y, n) in [(3, -2.4, 5), (5.2, -2.1, 3), (7.4, -2.6, 7), (9.2, -1.8, 4)]:
    for k in range(n):
        out.append(caja(x, y, k * 0.22, 1.1, 0.8, 0.16, arriba=dict(fill=GRIS), izq=dict(fill=VERDE), der=dict(fill='url(#trama-verde)')))


def figura(x, y, z, escala, color):
    cx, cy = p(x, y, z)
    s = escala
    return (f'<rect x="{cx - 13 * s:.1f}" y="{cy - 62 * s:.1f}" width="{26 * s:.1f}" height="{46 * s:.1f}" rx="{13 * s:.1f}" fill="{color}" stroke="{PAPEL}" stroke-width="4"/>'
            f'<circle cx="{cx:.1f}" cy="{cy - 76 * s:.1f}" r="{12 * s:.1f}" fill="{color}" stroke="{PAPEL}" stroke-width="4"/>')


# El subagente, leyendo dentro del archivo
out.append(figura(4.6, -3.4, 0, 0.9, GRIS))
bx, by = p(4.6, -3.4, 1.6)
out.append(f'<rect x="{bx - 26:.1f}" y="{by - 8:.1f}" width="34" height="24" fill="{VERDE}" transform="rotate(-12 {bx:.1f} {by:.1f})"/>')

# Escritorio pequeño delante a la izquierda, con la conversación principal
out.append(caja(-7.5, 2.5, 0, 3.4, 1.8, 1.5, arriba=dict(fill=GRIS), izq=gris_t, der=trama))
out.append(caja(-6.6, 2.7, 1.5, 1.6, 0.25, 1.3, arriba=lleno, izq=lleno, der=dict(fill=PAPEL, stroke=VERDE, stroke_width='3')))
out.append(figura(-8.4, 4.4, 0, 1.15, GRIS))

# El camino de vuelta: puntos de tinta verde y una sola nota doblada
a, b = p(4.0, -0.6, 0.4), p(-4.2, 3.4, 1.7)
c1, c2 = (a[0] - 120, a[1] + 210), (b[0] + 260, b[1] + 160)
out.append(f'<path d="M{a[0]:.1f},{a[1]:.1f} C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {b[0]:.1f},{b[1]:.1f}" '
           f'fill="none" stroke="{VERDE}" stroke-width="6" stroke-linecap="round" stroke-dasharray="0 22"/>')
t = 0.55
nx = (1 - t) ** 3 * a[0] + 3 * (1 - t) ** 2 * t * c1[0] + 3 * (1 - t) * t * t * c2[0] + t ** 3 * b[0]
ny = (1 - t) ** 3 * a[1] + 3 * (1 - t) ** 2 * t * c1[1] + 3 * (1 - t) * t * t * c2[1] + t ** 3 * b[1]
out.append(f'<g transform="translate({nx:.1f} {ny - 40:.1f}) rotate(-8)">'
           f'<polygon points="-34,-22 34,-22 34,22 -34,22" fill="{GRIS}"/>'
           f'<polygon points="14,-22 34,-22 34,-2" fill="{VERDE}"/>'
           f'<line x1="-22" y1="-6" x2="16" y2="-6" stroke="{PAPEL}" stroke-width="4"/>'
           f'<line x1="-22" y1="6" x2="6" y2="6" stroke="{PAPEL}" stroke-width="4"/></g>')

escena = '\n'.join(out)
print(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <pattern id="trama-verde" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(30)">
    <circle cx="4.5" cy="4.5" r="2.6" fill="{VERDE}"/></pattern>
  <pattern id="trama-gris" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(-30)">
    <circle cx="4" cy="4" r="1.9" fill="{GRIS}"/></pattern>
  <filter id="grano" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="3" result="r"/>
    <feColorMatrix in="r" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.3 1.5" result="m"/>
    <feComposite in="SourceGraphic" in2="m" operator="in"/></filter>
</defs>
<rect width="{W}" height="{H}" fill="{PAPEL}"/>
<g filter="url(#grano)" opacity=".35" transform="translate(5 3)">{escena}</g>
<g filter="url(#grano)">{escena}</g>
</svg>''')
