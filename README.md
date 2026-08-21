# meta-mcp

Reportes de rendimiento de Meta Ads generados a partir del Meta Ads MCP, publicados como sitio
estático en Vercel.

## Contenido

| Ruta | Descripción |
|---|---|
| `index.html` | Reporte de rendimiento — Nativo El Plomo, julio 2026 |
| `vercel.json` | Configuración de Vercel (URLs limpias, cabeceras `noindex`) |
| `docs/paid-media/PLAN-LEAD-GEN.md` | Plan de gestión y escalado para cuentas de lead gen (inmobiliaria, servicios, B2B) |
| `docs/paid-media/PLAN-ECOMMERCE.md` | Plan de gestión y escalado para ecommerce y retail (beauty, fashion, multicategoría) |
| `docs/paid-media/FICHA-CUENTA.md` | Plantilla de aterrizaje por cliente: identidad, economía, fase vigente, señal, línea base y guardarraíles |
| `.claude/skills/paid-media/` | Gestión recurrente Google Ads + Meta Ads: rutinas, escalado, señal, diagnóstico, entregables. Modo solo lectura |
| `.claude/skills/pauta-contenidos/` | Pauta mensual de contenidos y campañas por cuenta: mix, ángulos, volumen, calendario y briefs |
| `.claude/skills/ad-concepts/` | Conceptos, hooks, guiones y copys con specs 2026 para Google y Meta |
| `.claude/skills/creative-testing/` | Matriz de testeo, nomenclatura, UTMs y criterio para declarar ganador |
| `.claude/skills/cierre-mensual/` | Cierre de mes: extracción, veredicto, ficha actualizada y reporte del cliente |
| `.claude/skills/marca-intothecom/` | Identidad de la agencia: paleta, tipografía Be Vietnam Pro y tokens CSS |
| `.claude/skills/ad-creative/` · `copywriting/` | Versiones actualizadas de los skills de la cuenta: contexto de marca, specs 2026, hooks, message match y español LATAM |

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
