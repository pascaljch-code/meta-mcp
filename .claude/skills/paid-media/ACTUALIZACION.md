# Rutina de auto-actualización del skill

Objetivo: que el skill nunca recomiende una práctica que Google o Meta ya cambiaron.
Frecuencia: **mensual**, más cualquier anuncio grande. Duración: 20–30 min.

## 1. Buscar (últimos ~45 días)

**Google Ads**
1. `Google Ads updates <mes> <año>` · `Google Ads product changes <año>`
2. `Performance Max updates <año>` · `AI Max for Search <año>`
3. `Smart Bidding changes tCPA tROAS <año>`
4. `Google Ads conversion tracking Data Manager API enhanced conversions <año>`
5. `Google Ads policy update housing employment credit <año>`

**Meta Ads**
6. `Meta Ads updates <mes> <año>` · `Facebook ads changes <año>`
7. `Advantage+ changes <año>` · `Meta Andromeda creative strategy <año>`
8. `Meta attribution changes <año>` · `Meta CAPI event match quality <año>`
9. `Meta special ad categories <año>`

**Transversal**
10. Vertical o mercado del cliente cuando corresponda.

Peso de las fuentes: **support.google.com · business.google.com · blog.google · developers.facebook.com ·
facebook.com/business/help** (oficiales) → prensa especializada (ppc.land, searchengineland, socialmediatoday)
→ blogs de agencia (solo como dato comparativo, nunca como regla). Un dato de agencia sin respaldo oficial
se registra como "reportado".

## 2. Contrastar

Tres preguntas antes de escribir nada:

1. ¿Contradice algo que el skill afirma hoy? (`grep -rn "<término>" references/`)
2. ¿Cambia una **acción concreta** de la rutina, el escalado, el tracking o la lectura de resultados?
   Si no cambia ninguna acción, **no se registra**.
3. ¿Tiene fecha y fuente verificable? Sin eso, no entra.

## 3. Escribir

1. `references/CHANGELOG-plataformas.md`: entrada nueva arriba, en la sección de la plataforma que
   corresponde, con el formato existente. Actualizar la línea "Revisado el AAAA-MM-DD".
2. Corregir los archivos afectados (`rutinas.md`, `google-ads.md`, `meta-ads.md`, `senal-y-tracking.md`,
   `escalado.md`, `diagnostico.md`, `politicas-y-riesgos.md`, `verticales.md`). **Reemplazar** la práctica
   obsoleta; no acumular versiones contradictorias.
3. Actualizar `docs/paid-media/PLAN-LEAD-GEN.md` o `PLAN-ECOMMERCE.md` solo si cambia una fase, un criterio
   de salida o una regla dura.
4. Si cambió un número (umbral, ventana, límite), buscarlo en todo el conjunto:
   `grep -rn "<número>" .claude/skills/paid-media docs/paid-media`

## 4. Cerrar

- Commit: `skill(paid-media): actualización AAAA-MM`.
- Resumen en tres partes: **(a)** qué cambió en la plataforma · **(b)** qué cambia en nuestra operación ·
  **(c)** qué cuentas hay que revisar esta semana por este cambio.
- Si algo obliga a reconfigurar cuentas de clientes, encabezar con **ACCIÓN REQUERIDA** — y recordar que
  la reconfiguración la ejecuta el usuario, no el skill.

## 5. Programación

- **Manual**: paso 8 de la rutina mensual.
- **Routine mensual**: `create_trigger`, cron `17 13 2 * *`, con el prompt: *"Corre la rutina de
  `.claude/skills/paid-media/ACTUALIZACION.md` sobre el repo pascaljch-code/meta-mcp en la rama de trabajo
  (o la rama por defecto si ya está mergeada). Commitea, pushea y entrega el resumen de 3 partes."*
- **`/loop`** en semanas de anuncios grandes.

**Límite de seguridad**: la rutina actualiza archivos de este repo y nada más. No accede a cuentas para
modificarlas y no propone aplicar cambios automáticamente.
