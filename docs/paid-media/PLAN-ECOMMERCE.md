# Plan de gestión y escalado — Ecommerce y retail

Para cuentas cuyo resultado es una **transacción online**: beauty, fashion, retail generalista,
suscripción de producto. Plataformas: Google Ads y Meta Ads.

Para lead gen (inmobiliaria, servicios, B2B), ver `PLAN-LEAD-GEN.md`. La operación diaria/semanal
detallada vive en el skill `.claude/skills/paid-media/`.

> **Modo solo lectura.** Este plan se ejecuta extrayendo información de las cuentas y entregando
> propuestas. Los cambios los aplica el equipo del cliente o el gestor, nunca el asistente.

---

## La tesis

**El resultado no es el ROAS reportado, es el margen.** Una cuenta puede mostrar ROAS 6 y perder plata si
el valor de conversión es ingreso bruto, si las devoluciones no se descuentan, o si el crecimiento viene
solo de marca y retargeting.

Orden invariable: `señal correcta → catálogo y captura → valor real → escalado → demanda nueva`.

---

## 1. Contrato de datos

| Pieza | Requisito |
|---|---|
| Conversión primaria | Compra con **valor dinámico real** |
| Secundarias | Add to cart, inicio de checkout — solo observación |
| Valor | **Margen de contribución**: sin impuestos, sin envío, neto de devoluciones sistemáticas |
| Google | Enhanced conversions + Merchant Center vinculado y sano |
| Meta | Píxel + CAPI deduplicados por `event_id`; EMQ vigilado en el evento de compra |
| Catálogo / feed | Precio, stock y disponibilidad al día; títulos, atributos e imágenes trabajados |
| Segmentación de cliente | Distinguir **cliente nuevo vs. recurrente** en el reporte |

Dos errores que invalidan todo el análisis: valor = ingreso bruto (premia productos de mal margen) y
catálogo desactualizado (se manifiesta como "el ROAS cayó sin causa aparente").

---

## 2. Fases (se avanza por criterio, no por calendario)

**Fase 0 — Cimientos (días 1–10).** Auditoría de conversiones y de valor, Merchant Center y catálogo de
Meta sanos, CAPI deduplicado, separación de marca (Google) y de prospecting/retargeting (Meta), línea base
de 90 días con margen y devoluciones incluidos.
**Salida:** compra medida con valor correcto en ambas plataformas y catálogo sin errores bloqueantes.

**Fase 1 — Catálogo y captura (semanas 2–5).** El feed es el producto: títulos, atributos e imágenes son
la palanca nº1 antes de tocar cualquier puja. Google: Search de marca, Search genérico por categoría,
Shopping o PMax con feed. Meta: prospecting con catálogo + retargeting dinámico.
**Salida:** ≥50 conversiones/30 días por campaña en Google; ~50 eventos/semana por conjunto en Meta.

**Fase 2 — Valor real (semanas 5–9).** Migrar el valor a margen; segmentar feed por margen o rotación;
separar top sellers de cola larga; empezar a leer **ROAS de cliente nuevo** como métrica de crecimiento.
**Salida:** tROAS operando sobre margen y ROAS de cliente nuevo estable durante 3 semanas.

**Fase 3 — Escalado controlado (semanas 9–20).** En orden: destrabar lo limitado por presupuesto →
ampliar catálogo y ángulos creativos → ampliar geografía → aflojar tROAS → sumar formato.
**Salida:** +50% de inversión vs. línea base con margen dentro del ±15% del objetivo.

**Fase 4 — Demanda nueva (mes 5+).** Demand Gen + PMax es hoy la combinación de mejor rendimiento
reportado en ecommerce (20–30% de mejora en ROAS), pero exige feed impecable y separación de marca.
En Meta, prospecting frío sostenido con volumen creativo. Validar con incrementalidad.

**Fase 5 — Régimen.** Calendario comercial, refresco creativo por temporada, control de canibalización de
marca y retargeting, y realineación de objetivos ante cambios de plataforma.

---

## 3. KPIs, en orden de importancia

Margen de contribución → **ROAS de cliente nuevo** → CAC de cliente nuevo → ROAS mezclado → AOV →
tasa de conversión → tasa de devolución por categoría.

El ROAS mezclado se reporta, pero no se decide con él: premia al retargeting y esconde el estancamiento.

---

## 4. Reglas de escalado

- Presupuesto: **+20% por paso en Google** (7–14 días) · **+15–20% en Meta** (48–72 h).
- tROAS: **±10–15% por paso**, nunca junto a un cambio de presupuesto.
- Cambios ≥~30% reinician el aprendizaje; durante el aprendizaje el CPA corre 20–40% más alto.
- Google: ~50 conversiones/30 días para tROAS. Meta: ~50 eventos/semana por conjunto.
- **Meta es un problema de creatividad, no de configuración**: con Andromeda la creatividad define a quién
  se le muestra el anuncio. Referencia actual: 15–50+ creatividades activas, en 9:16, 1:1 y carrusel/catálogo.

### Árbol de decisión mensual

```
¿Margen / ROAS de cliente nuevo dentro del objetivo (±15%) en 30 días?
├── SÍ  → ¿limitada por presupuesto?  SÍ → +20%/+15–20%   ·   NO → aflojar tROAS, ampliar catálogo/geo o sumar formato
└── NO  → cuello de botella:
          Señal → valor real, devoluciones, EMQ, deduplicación
          Catálogo → títulos, atributos, imágenes, stock, precio
          Creatividad → fatiga, pocos ángulos, formatos faltantes
          Mix → crecimiento solo de marca o retargeting = no hay crecimiento
          Producto / precio → competencia, promoción, quiebres de stock. NO más presupuesto
          Operación → despacho, tiempos de entrega, post venta
```

---

## 5. Ajustes por categoría

- **Beauty:** ROAS de cliente nuevo + tasa de recompra; ciclo corto permite decisiones semanales;
  rotación creativa alta (es donde la fatiga aparece más rápido); cuidado con claims y "antes/después".
- **Fashion:** ROAS **neto de devoluciones**; catálogo con talla, color y stock impecable; calendario de
  colección y drops manda sobre la optimización fina; video de producto en movimiento.
- **Retail multicategoría:** ROAS por categoría, nunca global; separar top sellers de cola larga; revisión
  diaria de quiebres en lo que concentra el gasto.

---

## 6. Primeros 30 días

| Días | Acción |
|---|---|
| 1–2 | Accesos de solo lectura, auditoría de conversiones y de valor, línea base de 90 días con margen |
| 3–4 | Señal: enhanced conversions, CAPI deduplicado, consent, EMQ del evento de compra |
| 5–6 | Catálogo y feed: errores bloqueantes, títulos, atributos, imágenes, stock y precio |
| 7 | Estructura: marca separada, prospecting vs. retargeting, top sellers vs. cola larga |
| 8–10 | Fase 1: Search de marca y categoría, Shopping/PMax con feed, prospecting y retargeting dinámico en Meta |
| 11–17 | Rutina diaria + primera semanal completa. No se toca la puja |
| 18–21 | Primeras lecturas de margen por categoría; plan creativo con ángulos faltantes |
| 22–28 | Valor migrado a margen; tROAS con el ROAS real; segmentación de feed |
| 29–30 | Reporte del mes 1: margen, ROAS de cliente nuevo, cuello de botella, propuesta y presupuesto del mes 2 |

Desde el mes 2, el trabajo es la cadencia del skill aplicada sobre la fase vigente.
