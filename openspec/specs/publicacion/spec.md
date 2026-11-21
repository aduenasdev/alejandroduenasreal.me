# publicacion Specification

## Purpose

Cada cambio se comprueba en CI, se ve en una vista previa propia y llega a producción solo al fusionar en `main`,
con el mismo artefacto que se probó.

## Requirements

### Requirement: Comprobaciones en cada PR
Cada PR y cada push a `main` SHALL ejecutar `astro check`, el build, `openspec validate --all --strict` y la
comprobación de enlaces internos. Si cualquiera falla, el PR MUST NOT poder fusionarse.

#### Scenario: Un enlace interno roto
- **WHEN** un PR rompe un enlace interno
- **THEN** el job `comprobar` falla y la protección de `main` impide fusionar

#### Scenario: Una spec mal formada
- **WHEN** un PR añade un requisito sin escenario
- **THEN** el paso de OpenSpec falla y el PR no se puede fusionar

### Requirement: Vista previa por PR
Cada PR de una rama del propio repositorio SHALL desplegarse en Cloudflare Pages en una URL propia, que se comenta en
el PR. Las vistas previas MUST llevar `X-Robots-Tag: noindex`.

#### Scenario: Se abre un PR
- **WHEN** se abre un PR desde `feat/x`
- **THEN** aparece un comentario «Vista previa: https://…pages.dev» y esa URL sirve el sitio del PR

#### Scenario: Un PR desde un fork
- **WHEN** se abre un PR desde un fork
- **THEN** se ejecuta `comprobar` pero no se despliega nada

### Requirement: Producción solo desde main, con el mismo artefacto
Un push a `main` SHALL desplegar en producción el `dist` compilado y comprobado en el mismo workflow, sin volver a
compilar.

#### Scenario: Alejandro fusiona un PR
- **WHEN** Alejandro fusiona un PR
- **THEN** `https://alejandroduenasreal.me` sirve ese commit, y «Cómo se hace» muestra su hash corto

### Requirement: Release
Cada despliegue a producción SHALL crear una release `vAAAA.MM.DD-<sha>` con notas generadas a partir de los PR.

#### Scenario: Despliegue a producción
- **WHEN** termina bien el despliegue de un push a `main`
- **THEN** aparece en GitHub una release `vAAAA.MM.DD-<sha corto>` con las notas generadas

### Requirement: Vuelta atrás
El README y «Cómo se hace» SHALL documentar el revert normal y el rollback urgente en Cloudflare.

#### Scenario: Una versión mala en producción
- **WHEN** una versión publicada falla
- **THEN** el README explica cómo revertir el PR y cómo hacer *Rollback* en Cloudflare en segundos

### Requirement: Cabeceras
El sitio SHALL servir `X-Content-Type-Options`, `Referrer-Policy`, `X-Frame-Options`, `Permissions-Policy` y una CSP
sin errores en la consola.

#### Scenario: Se abre cualquier página
- **WHEN** se pide cualquier página del sitio
- **THEN** la respuesta lleva las cinco cabeceras y la consola del navegador no muestra errores de CSP

### Requirement: Analítica de visitas sin cookies
El dominio propio SHALL medir las visitas con Cloudflare Web Analytics, inyectado en el borde de Cloudflare, sin
cookies ni consulta de la URL. La CSP MUST permitir solo `https://static.cloudflareinsights.com` (script) y
`https://cloudflareinsights.com` (envío de datos) como orígenes externos para esa analítica. El repositorio MUST NOT
llevar el script ni el token del beacon, y las vistas previas de `*.pages.dev` MUST NOT medirse.

#### Scenario: CSP preparada para el beacon
- **WHEN** se pide cualquier página del sitio
- **THEN** la CSP lleva `https://static.cloudflareinsights.com` en `script-src` y `https://cloudflareinsights.com` en `connect-src`, y ningún otro origen externo nuevo

#### Scenario: Sin rastro en el repositorio
- **WHEN** se busca `cloudflareinsights` en `src/` y en `dist/`
- **THEN** no aparece: el beacon solo lo añade Cloudflare en el dominio propio
