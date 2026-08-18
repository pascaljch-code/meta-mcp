# meta-mcp

Reportes de rendimiento de Meta Ads generados a partir del Meta Ads MCP, publicados como sitio
estático en Vercel.

## Contenido

| Ruta | Descripción |
|---|---|
| `index.html` | Reporte de rendimiento — Nativo El Plomo, julio 2026 |
| `vercel.json` | Configuración de Vercel (URLs limpias, cabeceras `noindex`) |
| `docs/google-ads/PLAN-GESTION.md` | Plan de gestión recurrente y escalado de cuentas de Google Ads (inmobiliaria + ecommerce) |
| `.claude/skills/google-ads-inmobiliaria/` | Skill operativo: rutinas diaria/semanal/mensual, escalado, tracking, diagnóstico y auto-actualización |

## Despliegue

Sitio estático sin build step. Vercel sirve `index.html` directamente desde la raíz del repo.

- **Framework preset:** Other
- **Build command:** ninguno
- **Output directory:** raíz (`.`)

Cada push a la rama por defecto dispara un despliegue de producción; el resto de las ramas generan
despliegues de vista previa.

## Aviso sobre los datos

Los reportes contienen datos de rendimiento publicitario de clientes (inversión, leads, costos por
resultado). Un despliegue de Vercel es **público por defecto**: cualquiera con la URL puede abrirlo.
Se recomienda activar la protección de despliegue en Vercel
(*Project Settings → Deployment Protection*) antes de compartir el enlace.

Las cabeceras `X-Robots-Tag: noindex, nofollow` evitan la indexación en buscadores, pero **no**
restringen el acceso a quien tenga el enlace.
