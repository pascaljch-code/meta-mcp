# Plan de gestión y escalado — Lead gen

Para cuentas cuyo resultado es un **lead que se convierte en venta con intervención comercial**:
inmobiliarias y proyectos, servicios profesionales, B2B. Plataformas: Google Ads y Meta Ads.

Para ecommerce y retail, ver `PLAN-ECOMMERCE.md`. La operación diaria/semanal detallada vive en el skill
`.claude/skills/paid-media/`.

> **Modo solo lectura.** Este plan se ejecuta extrayendo información de las cuentas y entregando
> propuestas. Los cambios los aplica el equipo del cliente o el gestor, nunca el asistente.

---

## La tesis

**El resultado no es el lead, es el lead calificado.** Todo el plan existe para que las plataformas
aprendan a comprar el perfil que el equipo comercial logra cerrar, no el formulario más barato.

Orden invariable: `señal correcta → captura de demanda → calidad del lead → escalado → demanda nueva`.

---

## 1. Contrato de datos (bloquea todo lo demás)

| Pieza | Requisito |
|---|---|
| Conversión primaria | **Lead calificado** (etapa del CRM), no "formulario enviado" |
| Secundarias | Formulario, llamada >60s, WhatsApp, agendamiento — solo observación |
| Google | Enhanced conversions (web y leads); Consent Mode v2 si hay tráfico EEA/UK |
| Meta | Píxel + CAPI deduplicados; EMQ vigilado en el evento de lead |
| CRM | Guarda GCLID/GBRAID/WBRAID y fbclid por lead, etapa y fecha |
| Ventana | 63 días desde el último clic para importar conversiones offline |
| SLA comercial | Primer contacto ≤5 minutos en horario hábil |

**Si el CRM no guarda el identificador de clic, no existe importación offline ni puja por valor.**
Es el bloqueo más común y el que más caro sale: sin él, el resto del plan no se puede ejecutar.

### Escala de valor por etapa (índice, no dinero)

| Etapa | Conversión | Valor |
|---|---|---|
| Formulario enviado | Lead | 1 |
| Contactado | Lead contactado | 5 |
| Calificado (presupuesto/financiamiento OK) | **Lead calificado** ← primaria | 25 |
| Visita o reunión agendada | Agendado | 60 |
| Visita o reunión realizada | Realizado | 120 |
| Reserva / propuesta aceptada | Reserva | 600 |
| Venta cerrada | Venta | 3000 |

Recalibrar cada trimestre contra las tasas reales de conversión entre etapas.

---

## 2. Fases (se avanza por criterio, no por calendario)

**Fase 0 — Cimientos (días 1–10).** Auditoría de conversiones, señal en ambas plataformas, separación de
marca (Google) y de prospecting/retargeting (Meta), negativos de cuenta, landing por intención con
formulario de 3–5 campos y 1–2 preguntas calificadoras, CRM con identificador de clic y etapas.
**Salida:** prueba completa clic → lead → CRM → conversión importada, y línea base de 90 días documentada.

**Fase 1 — Captura de demanda (semanas 2–5).** Google Search por intención es el motor; Meta aporta
demanda latente con creatividad. Puja: `Maximizar conversiones` 2–3 semanas y luego tCPA con el **CPA real**.
Remarketing activo desde el día uno.
**Salida:** ≥30 conversiones primarias/30 días por campaña en Google; ~50 eventos/semana por conjunto en Meta.

**Fase 2 — Calidad del lead (semanas 5–9).** Importación de etapas del CRM; la primaria migra de formulario
a lead calificado; el análisis semanal cruza términos, públicos y creatividades **con calidad**, no con volumen.
**Salida:** ≥30 "lead calificado"/30 días y % de calificados estable o al alza durante 3 semanas.

**Fase 3 — Escalado controlado (semanas 9–20).** En orden: destrabar lo limitado por presupuesto → ampliar
intención y ángulos creativos → ampliar geografía → aflojar objetivo → sumar formato (PMax con señal de
calidad, Advantage+ acotado).
**Salida:** +50% de inversión vs. línea base con CPL calificado dentro del ±15% del objetivo.

**Fase 4 — Demanda nueva (mes 5+).** Demand Gen y YouTube en Google; prospecting frío con volumen creativo
en Meta. Se valida con incrementalidad (geo-holdout o lift), no con atribución de último clic.

**Fase 5 — Régimen.** Refresco creativo, control de canibalización de marca, auditoría de calidad de lead
y realineación de objetivos cada vez que cambian las reglas de plataforma.

---

## 3. KPIs, en orden de importancia

Costo por **lead calificado** → costo por reunión/visita → costo por reserva → % de calificados sobre el
total → tiempo al primer contacto → CPL bruto (último, y solo como control de eficiencia de tráfico).

La referencia es la **línea base propia** de 90 días. Los benchmarks externos sirven para sanidad de orden
de magnitud, nunca como promesa: el objetivo se deriva de ticket × margen × tasa de cierre.

---

## 4. Reglas de escalado

- Presupuesto: **+20% por paso en Google** (7–14 días de estabilización) · **+15–20% en Meta** (48–72 h).
- Objetivos: **±10–15% por paso**, nunca junto a un cambio de presupuesto.
- Cambios ≥~30% de presupuesto reinician el aprendizaje.
- No se juzga rendimiento en fase de aprendizaje: el CPA corre 20–40% por encima del estado estable.
- Con poco volumen, **consolidar** antes que segmentar.

### Árbol de decisión mensual

```
¿CPL calificado dentro del objetivo (±15%) en 30 días?
├── SÍ  → ¿limitada por presupuesto?  SÍ → +20%/+15–20%   ·   NO → aflojar objetivo, ampliar cobertura o sumar formato
└── NO  → cuello de botella:
          Señal → primaria, importación de etapas, EMQ, consolidar
          Tráfico → negativos y exclusiones (Google) · públicos y solapamiento (Meta)
          Creatividad → ángulos y formatos nuevos (causa nº1 en Meta)
          Landing → CRO, formulario, velocidad. NO más presupuesto
          Comercial → SLA ≤5 min, guion, seguimiento. Se documenta, NO se compensa con presupuesto
```

---

## 5. Riesgo específico del vertical

En **EE.UU. y Canadá**, vivienda es categoría especial en ambas plataformas: sin segmentación por edad,
género, código postal (ni ingresos en Meta), y con restricciones sobre audiencias propias en Demand Gen.
La estrategia se sostiene en intención, geografía amplia y creatividad. Marcar mal la categoría es causa
de cierre de cuenta.

---

## 6. Primeros 30 días

| Días | Acción |
|---|---|
| 1–2 | Accesos de solo lectura, auditoría de conversiones, línea base de 90 días |
| 3–4 | Señal: enhanced conversions, CAPI, consent, identificador de clic en el CRM, prueba end-to-end |
| 5 | Negativos de cuenta, exclusiones de marca, revisión de estructura |
| 6–7 | Landings y formulario (3–5 campos + calificadoras), página de gracias medida |
| 8–10 | Fase 1: Search por intención, remarketing, prospecting de Meta con 2–3 ángulos |
| 11–17 | Rutina diaria + primera semanal completa. No se toca la puja |
| 18–21 | Primeros negativos con datos, hipótesis de landing, alta de etapas en el CRM |
| 22–28 | tCPA con el CPA real; activar importación de etapas |
| 29–30 | Reporte del mes 1: línea base vs. mes 1, cuello de botella nombrado, propuesta y presupuesto del mes 2 |

Desde el mes 2, el trabajo es la cadencia del skill aplicada sobre la fase vigente.
