# Plan de gestión recurrente y escalado — Google Ads

Modelo operativo para gestionar cuentas de Google Ads de forma recurrente, con dos objetivos de
negocio en paralelo:

- **Ecommerce** → optimización a **valor** (ROAS, margen, AOV).
- **Inmobiliarias / lead gen** → optimización a **lead calificado y venta**, no a volumen de formularios.

El plan tiene dos capas que se usan juntas:

1. **Fases** (dónde está la cuenta en su madurez) → qué te toca construir ahora.
2. **Cadencia** (diaria / semanal / mensual / trimestral) → qué se revisa siempre, sin importar la fase.

> Regla base de todo el documento: **una cuenta no se escala por presupuesto, se escala por datos.**
> Primero se arregla la señal (conversiones y su valor), después se sube la inversión.

---

## 0. Antes de tocar la cuenta: el contrato de datos

Nada de lo que sigue funciona sin esto. Si falta, esta es la primera tarea del mes 1.

| Requisito | Ecommerce | Inmobiliaria |
|---|---|---|
| Conversión principal única | Compra (con valor dinámico real) | **Lead calificado** (no "envío de formulario") |
| Conversiones secundarias | Add to cart, inicio de checkout (solo observación) | Formulario, llamada >60s, WhatsApp, visita agendada |
| Enhanced Conversions | Obligatorio (web) | Obligatorio (web **y** leads) |
| Consent Mode v2 | Obligatorio si hay tráfico EEA/UK | Obligatorio si hay tráfico EEA/UK |
| GCLID / GBRAID / WBRAID en CRM | Deseable | **Crítico**: sin GCLID guardado en el CRM no existe importación offline ni puja por valor |
| Valor por etapa del embudo | Precio - costo | Score de lead (ver §3.2) |
| Ventana de subida offline | — | Máx. 63 días desde el último clic |

Cambios de plataforma vigentes que afectan este contrato (ver `.claude/skills/google-ads-inmobiliaria/references/CHANGELOG-plataforma.md`):

- Las subidas de **offline conversion import** y **enhanced conversions for leads** migran a la
  **Data Manager API**; el camino recomendado hoy es *enhanced conversions for leads* en lugar de OCI clásico.
- Desde **junio 2026**, enhanced conversions de web y de leads se unifican en un solo interruptor.
- Desde **abril 2026** Google acepta datos de usuario simultáneamente desde tag, Data Manager y API.
- Desde el **17 de agosto de 2026**, las campañas limitadas por presupuesto con tCPA/tROAS dejan de
  buscar rendimiento *mejor* que el objetivo y apuntan al número exacto configurado → **los objetivos
  históricamente conservadores ahora encarecen el CPA real**. Hay que realinear objetivos al rendimiento real.

---

## 1. Fases de la cuenta

Cada fase tiene **criterio de salida**. No se avanza por calendario, se avanza por criterio cumplido.

### Fase 0 — Diagnóstico y cimientos (días 1–10)

Objetivo: dejar la cuenta medible y limpia. No se busca rendimiento todavía.

1. Auditoría de conversiones: una sola conversión primaria, deduplicada, sin conversiones "basura"
   (pageviews, clics en teléfono sin duración) contando como primarias.
2. Enhanced conversions + Consent Mode v2 + GA4 vinculado + Merchant Center vinculado (ecommerce).
3. Estructura: consolidar campañas redundantes; separar **Marca** de **Genérico** siempre.
4. Listas de negativos a nivel cuenta (empleo, gratis, DIY, competidores no deseados, "planos gratis",
   "arriendo" si solo se vende, etc.).
5. Exclusiones de marca y negativos en PMax (hoy hasta 10.000 negativos por campaña).
6. Landing pages: velocidad, formulario de 3–5 campos, 1–2 preguntas calificadoras, thank-you page con evento.
7. CRM: campos GCLID, fuente, etapa, valor; SLA de contacto **≤5 minutos** en horario hábil.
8. Línea base documentada: CPA/CPL, CVR, ROAS, % leads calificados, tiempo de contacto, últimos 90 días.

**Salida:** tracking verificado con test end-to-end (clic → lead → CRM → conversión importada) y línea base firmada.

### Fase 1 — Captura de demanda (semanas 2–5)

Objetivo: comprar la demanda que ya existe, al costo más bajo posible, con datos limpios.

- **Inmobiliaria:** Search por intención, no por producto. 4 ejes clásicos que funcionan:
  `Marca` · `Proyecto/Producto + Ubicación` · `Categoría + Ubicación` (ej. "departamentos nuevos Ñuñoa")
  · `Intención financiera` (ej. "subsidio", "crédito hipotecario", "inversión con arriendo garantizado").
  Un ad group por intención cerrada, 1 landing por intención.
- **Ecommerce:** Search de marca + Search genérico por categoría + Shopping estándar (o PMax solo-feed si ya hay datos).
- Puja: `Maximizar conversiones` sin objetivo las primeras 2–3 semanas → luego tCPA/tROAS con el
  **rendimiento real** como objetivo.
- Remarketing siempre encendido (baja el CPL 20–40% en inmobiliaria).
- Presupuesto: 70–80% en captura de demanda, 20–30% en pruebas.

**Salida:** ≥30 conversiones primarias/30 días por campaña con tCPA (≥50 si se usará tROAS).

### Fase 2 — Calidad y valor (semanas 5–9)

Objetivo: que el algoritmo aprenda a comprar **el lead que se cierra**, no el que se envía.

- Activar importación offline / enhanced conversions for leads con las etapas del CRM.
- Migrar la conversión primaria de "formulario" a "**lead calificado**".
- Implementar valores por etapa (§3.2) y pasar a **tROAS** o `Maximizar valor de conversión`.
- Análisis semanal de términos de búsqueda **cruzado con calidad de lead**, no solo con volumen.
- Ecommerce: valor = margen, no ingreso. Excluir devoluciones recurrentes de la señal.

**Salida:** ≥30 conversiones "lead calificado"/30 días y % de leads calificados estable o al alza durante 3 semanas.

### Fase 3 — Escalado controlado (semanas 9–20)

Objetivo: subir inversión sin destruir eficiencia. Ver reglas duras en §4.

Orden de escalado (siempre en este orden, no saltarse pasos):

1. **Quitar límite de presupuesto** en lo que ya es rentable (campañas "limitadas por presupuesto").
2. **Ampliar cobertura de intención** (más keywords/temas de búsqueda de la misma familia que ya convierte).
3. **Ampliar geografía** (comunas/ciudades vecinas, o nacional para proyectos de inversión).
4. **Aflojar el objetivo** tCPA/tROAS de forma escalonada para comprar más volumen.
5. **Sumar formatos**: PMax (con feed o con señales de audiencia), Demand Gen, YouTube.

**Salida:** +50% de inversión vs. línea base con CPA/ROAS dentro del ±15% del objetivo.

### Fase 4 — Generación de demanda (mes 5 en adelante)

- **Demand Gen** (YouTube, Discover, Gmail) para llenar el embudo alto: en inmobiliaria funciona para
  proyectos en verde/preventa y para inversión, siempre con lead calificado como señal.
- **PMax** como cosechador de fondo de embudo; nunca como primer motor sin datos.
- Medición de incrementalidad: experimentos de geo-holdout o lift antes de creer la atribución.
- Ecommerce: PMax + Demand Gen combinados es la dupla del año (ganancias reportadas de 20–30% en ROAS),
  pero exige feed impecable y separación de marca.

### Fase 5 — Régimen (continuo)

La cuenta ya no se "construye", se **defiende**: refresco creativo, control de canibalización de marca,
auditoría de calidad de lead, y re-alineación de objetivos cada vez que Google cambia las reglas.

---

## 2. Cadencia operativa

### 2.1 Diaria — 10 a 15 minutos por cuenta

Nunca optimizar de verdad en esta ventana. La rutina diaria es **detección de incendios**, no ajuste fino.

1. **Gasto y ritmo**: ¿alguna campaña gastó >130% o <60% de lo esperado ayer?
2. **Tracking vivo**: ¿hubo conversiones ayer? Cero conversiones en una cuenta activa = fallo de tag hasta que se demuestre lo contrario.
3. **Rechazos y alertas**: anuncios desaprobados, políticas, extensiones rechazadas, feed con errores (ecommerce).
4. **Leads del día**: ¿llegaron al CRM? ¿se contactaron en ≤5 min? ¿hay leads basura evidentes (spam, bots, otra ciudad)?
5. **Términos de búsqueda de emergencia**: solo los de gasto alto y 0 conversiones que aparecieron ayer → negativo inmediato.
6. Registrar cualquier cambio en el **log de cambios** (fecha, campaña, qué, por qué, hipótesis).

Bandera roja que rompe la rutina y se atiende hoy mismo: conversiones caídas a 0, CPA diario >2× objetivo con
gasto significativo, o campaña principal detenida por facturación/política.

### 2.2 Semanal — 60 a 90 minutos por cuenta (día fijo, ej. martes)

Este es el bloque donde se optimiza. Orden recomendado:

1. **Términos de búsqueda** (Search, PMax y AI Max): negativos por irrelevancia y por *mala calidad de lead*.
   Promover a keyword propia los términos con buena conversión.
2. **Calidad de lead** (inmobiliaria): marcar en el CRM la semana anterior (crudo / contactado / calificado /
   visita / reserva) y subir esas etapas a Google. Sin este paso, la Fase 2 nunca madura.
3. **Presupuestos**: mover dinero desde lo que no convierte hacia lo limitado por presupuesto y rentable.
4. **Objetivos de puja**: revisar tCPA/tROAS vs. real de los últimos 14 días. Ajuste máximo 10–15% por semana.
5. **Assets y anuncios**: RSA con calificación "Buena/Excelente", pausar el peor asset solo con datos suficientes;
   revisar assets de PMax por grupo y por canal.
6. **Audiencias y señales**: listas de clientes actualizadas, exclusión de convertidos, exclusión de listas 1P donde corresponda.
7. **Landing / CRO**: 1 hipótesis de mejora por semana (headline, formulario, prueba social, velocidad).
8. **Competencia**: Auction Insights — si un competidor subió cuota de impresiones, esperar CPC al alza y decidir si se pelea.
9. **Experimentos**: revisar los activos; no concluir antes de 2 semanas o significancia.

Regla de oro semanal: **máximo 2–3 cambios estructurales por campaña por semana.** Más que eso y no se puede
atribuir el resultado a nada.

### 2.3 Mensual — 2 a 4 horas por cuenta

1. **Reporte de resultados** (usar plantilla del skill): inversión, leads, leads calificados, CPL, CPL calificado,
   visitas, reservas/ventas, ROAS o ROI del mes; comparación vs. mes anterior y vs. objetivo.
2. **Diagnóstico del embudo**: ¿el problema del mes fue tráfico, landing, calidad de lead o seguimiento comercial?
   El reporte debe nombrar el cuello de botella, no solo mostrar números.
3. **Decisión de escalado**: aplicar el árbol de decisión de §4.1 y fijar el presupuesto del mes siguiente.
4. **Refresco creativo**: nuevas variantes de anuncios/creativos (obligatorio en Demand Gen y YouTube por fatiga).
5. **Revisión estructural**: ¿hay que abrir campaña nueva (proyecto nuevo, categoría nueva, ciudad nueva)?
   ¿Consolidar campañas con poco volumen que nunca salen de aprendizaje?
6. **Realineación de objetivos**: comparar tCPA/tROAS configurados con el rendimiento real de 30 días.
7. **Higiene**: negativos acumulados, keywords con 0 impresiones, presupuestos compartidos huérfanos,
   conversiones duplicadas, redirecciones rotas.
8. **Actualización de mejores prácticas**: correr la rutina de auto-actualización del skill (§5).

### 2.4 Trimestral

- Auditoría profunda de cuenta (estructura, señal, políticas, canibalización de marca).
- **Prueba de incrementalidad**: apagar marca o una geografía en holdout y medir el efecto real.
- Revisión de política y riesgo: sector vivienda tiene targeting restringido en **EE.UU. y Canadá**
  (no se puede segmentar por edad, género, estado civil, parentalidad ni por ZIP code) y las campañas
  Demand Gen/Discovery con audiencias propias pueden verse limitadas en categorías sensibles.
  Si el cliente opera en esos países, esto define la estrategia de audiencias.
- Plan del trimestre: nuevos proyectos, estacionalidad, presupuesto anual, objetivos comerciales del cliente.

---

## 3. Cómo se mide el éxito

### 3.1 KPIs por vertical

**Inmobiliaria** (en orden de importancia): costo por lead calificado → costo por visita agendada →
costo por reserva → % de leads calificados sobre total → tiempo de primer contacto → CPL bruto.
Referencia 2026 de operadores con buen desempeño: CPL mezclado ~USD 18–55 según mercado y ticket;
en LATAM el rango útil se calibra con la línea base propia, no con benchmarks importados.

**Ecommerce**: ROAS y margen de contribución → CPA por nuevo cliente → AOV → tasa de conversión de sesión →
% de ingreso de marca vs. no-marca (si sube el de marca, probablemente no estás creciendo, solo cosechando).

### 3.2 Valores por etapa (inmobiliaria) — la pieza que hace funcionar la puja por valor

Se sube al Google Ads el mismo lead varias veces, con la etapa como conversión y un valor creciente
(índice relativo, no dinero real, para no exponer precios):

| Etapa CRM | Conversión | Valor índice |
|---|---|---|
| Formulario enviado | Lead | 1 |
| Contactado | Lead contactado | 5 |
| Calificado (presupuesto/financiamiento OK) | **Lead calificado** ← primaria | 25 |
| Visita agendada | Visita agendada | 60 |
| Visita realizada | Visita realizada | 120 |
| Reserva / promesa | Reserva | 600 |
| Escritura / venta | Venta | 3000 |

Con esto, `Maximizar valor de conversión` con tROAS empieza a comprar el perfil que efectivamente compra.
La escala debe reflejar la probabilidad real de cierre de cada etapa; se recalibra cada trimestre.

---

## 4. Reglas duras de escalado

- **Presupuesto: +20% por paso, máximo.** Esperar 7–14 días de estabilización antes del siguiente paso.
  Cambios de ~30% o más pueden reiniciar el aprendizaje.
- **Objetivos (tCPA/tROAS): ±10–15% por paso**, y nunca en la misma semana que un cambio de presupuesto.
- **Un cambio por variable a la vez.** Presupuesto o puja, no ambos.
- **No tocar nada durante el aprendizaje** (≈7 días o hasta ~30 conversiones desde el último cambio estructural).
- **Volumen mínimo para automatizar**: ~30 conversiones/30 días para tCPA, ~50 para tROAS.
- **PMax necesita 6 semanas** antes de cambios mayores; PMax sin datos de conversión de calidad canibaliza marca.
- Si algo se rompe al escalar: **volver al último escalón estable**, no seguir bajando el objetivo.

### 4.1 Árbol de decisión mensual

```
¿CPA/ROAS dentro del objetivo (±15%) los últimos 30 días?
├── SÍ  → ¿La campaña está limitada por presupuesto?
│         ├── SÍ  → subir presupuesto +20% (siguiente paso en 7–14 días)
│         └── NO  → aflojar objetivo 10% O ampliar intención/geografía O sumar formato (Fase 3/4)
└── NO  → ¿El problema es volumen de señal o calidad de tráfico?
          ├── Señal (pocas conversiones)   → volver a Fase 2: valor por etapa, ECL, consolidar campañas
          ├── Calidad de tráfico            → negativos, exclusiones de marca, revisar PMax/AI Max, geo
          ├── Landing (CVR bajo con buen CTR) → CRO, no más presupuesto
          └── Comercial (leads buenos, cero cierres) → SLA de contacto y guion de venta del cliente
```

Si el cuello de botella es del cliente (no contactan los leads), se documenta y se comunica en el reporte:
inyectar más presupuesto sobre un embudo comercial roto solo destruye la cuenta y la relación.

---

## 5. Auto-actualización de mejores prácticas

Google cambia las reglas varias veces al año (el cambio de Smart Bidding del 17 de agosto de 2026 es un
ejemplo: invalidó de golpe una práctica estándar de poner objetivos conservadores). Por eso el skill
`google-ads-inmobiliaria` incluye una rutina de actualización mensual que:

1. Busca cambios de producto y política de los últimos ~45 días.
2. Contrasta cada hallazgo con lo que dice el skill.
3. Escribe el hallazgo con fecha y fuente en `references/CHANGELOG-plataforma.md`.
4. Corrige los archivos del skill cuando una práctica queda obsoleta.
5. Deja un resumen de "qué cambia en tu operación" para revisión humana.

Ver `.claude/skills/google-ads-inmobiliaria/ACTUALIZACION.md`.

---

## 6. Primeros 30 días, día por día (resumen ejecutable)

| Día | Acción |
|---|---|
| 1–2 | Accesos, auditoría de conversiones, línea base de 90 días |
| 3–4 | Arreglo de tracking: EC, Consent Mode v2, GA4, GCLID en CRM, test end-to-end |
| 5 | Negativos de cuenta, exclusiones de marca, limpieza de estructura |
| 6–7 | Landings e formulario (3–5 campos + calificadoras), thank-you page medida |
| 8–10 | Lanzamiento Fase 1: Marca, Genérico por intención, Remarketing. `Maximizar conversiones` |
| 11–17 | Rutina diaria + primera rutina semanal completa. No tocar pujas |
| 18–21 | Primeros negativos con datos, primeras hipótesis de landing, alta de etapas en CRM |
| 22–28 | Pasar a tCPA con el CPA real; activar importación de etapas de CRM |
| 29–30 | Reporte mes 1: línea base vs. mes 1, cuello de botella nombrado, plan y presupuesto del mes 2 |

A partir del mes 2, el trabajo es exactamente la cadencia de §2 aplicada sobre la fase en que esté la cuenta.
