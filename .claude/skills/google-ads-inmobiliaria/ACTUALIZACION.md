# Rutina de auto-actualización del skill

Objetivo: que este skill nunca recomiende una práctica que Google ya cambió. Se corre **una vez al mes**
(y ante cualquier anuncio grande de Google). Duración: 20–30 min.

Puede correrla una persona, una sesión manual (`/google-ads-inmobiliaria actualiza el skill`), o una
Routine programada (ver §5).

---

## 1. Buscar (últimos ~45 días)

Ejecuta estas búsquedas web y quédate con lo publicado o vigente en la ventana:

1. `Google Ads updates <mes> <año>` y `Google Ads product changes <mes> <año>`
2. `Performance Max updates <año>` · `AI Max for Search updates <año>`
3. `Smart Bidding changes tCPA tROAS <año>`
4. `Google Ads conversion tracking changes enhanced conversions Data Manager API <año>`
5. `Google Ads policy update housing employment credit <año>`
6. `Demand Gen best practices <año>`
7. `Google Ads lead generation benchmarks real estate <año>`
8. Vertical del cliente: `Google Ads inmobiliaria <país> <año>`

Fuentes de mayor peso, en orden: **support.google.com** y **business.google.com** y **blog.google**
(oficiales) → **developers.google.com/google-ads** (API) → prensa especializada (ppc.land,
searchengineland, storegrowers) → blogs de agencia (solo para datos comparativos, nunca para reglas).

Un dato de blog de agencia sin respaldo oficial se registra como "reportado", no como regla.

## 2. Contrastar

Para cada hallazgo, responde tres preguntas antes de escribir nada:

1. **¿Contradice algo que este skill afirma hoy?** (grep el término en `references/`)
2. **¿Cambia una acción concreta de la rutina, del escalado o del tracking?** Si no cambia ninguna acción,
   **no se registra**. El changelog no es un feed de noticias.
3. **¿Tiene fecha y fuente verificable?** Sin eso, no entra.

## 3. Escribir

En este orden:

1. **`references/CHANGELOG-plataforma.md`**: agregar la entrada arriba, con el formato existente
   (fecha del cambio · qué cambió · **qué hacemos distinto** · fuente). Actualizar la línea
   "Revisado el AAAA-MM-DD".
2. **Corregir los archivos afectados** (`rutinas.md`, `escalado.md`, `tracking-y-datos.md`,
   `estructura-y-fases.md`, `politicas-y-riesgos.md`, `diagnostico.md`). Reemplazar la práctica obsoleta,
   no acumular versiones contradictorias.
3. **`docs/google-ads/PLAN-GESTION.md`**: actualizar solo si cambia una fase, un criterio de salida o
   una regla dura.
4. Si un número (umbral, ventana, límite) cambió, buscarlo en **todos** los archivos:
   `grep -rn "<número>" .claude/skills/google-ads-inmobiliaria docs/google-ads`

## 4. Cerrar

- Commit en la rama de trabajo con mensaje `skill(google-ads): actualización AAAA-MM`.
- Resumen para revisión humana con tres secciones:
  **(a)** qué cambió en la plataforma, **(b)** qué cambia en nuestra operación,
  **(c)** qué cuentas hay que tocar esta semana por este cambio.
- Si un cambio obliga a reconfigurar cuentas de clientes (ej. migración de API, política nueva),
  márcalo como **ACCIÓN REQUERIDA** al inicio del resumen.

## 5. Programación

Opciones, de menor a mayor automatización:

- **Manual**: correr esta rutina en el bloque mensual de cada cuenta (paso 8 de la rutina mensual).
- **Routine mensual** (sesión en la nube que corre sola y commitea a la rama):
  crear con la herramienta `create_trigger` — cron `17 13 2 * *` (día 2 de cada mes, 13:17 UTC),
  con el prompt: *"Corre la rutina de `.claude/skills/google-ads-inmobiliaria/ACTUALIZACION.md` sobre el
  repo pascaljch-code/meta-mcp, rama `claude/google-ads-management-plan-vrflqq` (o la rama por defecto si
  ya está mergeada). Commitea y pushea los cambios y entrega el resumen de 3 secciones."*
- **`/loop`** dentro de una sesión activa para revisiones más frecuentes en semanas de anuncios
  (Google Marketing Live, cambios de política).

Regla de seguridad: la Routine **propone y commitea en una rama**, nunca reconfigura cuentas de clientes.
Cualquier cambio en cuentas reales pasa por revisión humana.
