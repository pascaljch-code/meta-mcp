---
name: pauta-contenidos
description: "Genera la pauta mensual de contenidos y campañas de una cuenta publicitaria: qué campañas se sostienen, qué mensajes se comunican, cuántas piezas se producen, en qué formatos y con qué calendario, para Google Ads y Meta Ads. Úsalo cuando el usuario pida la 'pauta del mes', 'planificación de contenidos', 'plan de campañas', 'qué anuncios hacemos este mes', 'calendario de publicaciones', 'plan creativo', 'brief del mes', 'necesito piezas nuevas', 'se nos fatigó la creatividad' o 'qué comunicamos en [mes]'. Se aterriza siempre en la ficha de marca y en la fase de la cuenta; entrega el plan y los briefs, nunca ejecuta cambios en las plataformas."
---

# Pauta mensual de contenidos y campañas

Traduces el estado real de una cuenta en un **plan de comunicación del mes**: qué se dice, a quién,
en qué formato, cuántas piezas y cuándo. No es un calendario decorativo — es la orden de producción
que alimenta la inversión del mes.

## Regla nº1 — Modo solo lectura

Extraes datos de las cuentas para decidir, y entregas plan y briefs. **Nunca creas, pausas ni modificas
campañas ni anuncios en las plataformas.** El usuario ejecuta.

## Regla nº2 — Nada se planifica sin ficha

Antes de proponer un solo mensaje, carga `references/ficha-marca.md` de esa cuenta. Si no existe,
levántala: pregunta lo que falte **en un solo bloque** y déjala escrita. Un plan sin ficha es un plan
genérico, y un plan genérico produce anuncios que podrían ser de cualquier marca.

Si falta información y el usuario no puede darla ahora, entrega el plan marcando explícitamente cada
supuesto como **[SUPUESTO — validar]**. Nunca inventes cifras, precios, testimonios ni diferenciales.

---

## Proceso (en este orden)

### 1. Contexto — de dónde salen las decisiones

| Fuente | Qué te da |
|---|---|
| Ficha de marca y cuenta | Voz, prueba, objeciones, límites, activos, fase, KPI del mes |
| Datos de la cuenta (MCP, solo lectura) | Qué ángulos y formatos rindieron, qué fatigó, dónde está el gasto |
| Cierre del mes anterior | Cuello de botella declarado y las 3 prioridades del mes |
| Calendario comercial del cliente | Lanzamientos, temporada, promociones, fechas duras |

Si no tienes acceso a los datos, pídelos o trabaja con lo que el usuario reporte, dejándolo dicho.

### 2. Objetivo del mes — uno, no cinco

Se deriva de la fase de la cuenta y del cuello de botella, no del entusiasmo:

| Fase | Objetivo típico del mes | Qué domina la pauta |
|---|---|---|
| 0–1 · cimientos y captura | Validar mensajes y capturar demanda existente | Pocos ángulos, muy claros, orientados a intención |
| 2 · calidad | Mejorar el perfil de quien convierte | Ángulos calificadores: precio, requisitos, para quién SÍ y para quién NO |
| 3 · escalado | Sostener más inversión sin subir el costo | Más variaciones de lo que ya gana + 1–2 apuestas nuevas |
| 4 · demanda nueva | Entrar a públicos que aún no buscan | Contenido de demanda: educación, deseo, prueba social, video |
| 5 · régimen | Defender eficiencia y evitar fatiga | Rotación programada y renovación de ganadores |

### 3. Mix del mes

Reparte antes de escribir nada:

- **Por etapa**: captura de demanda · retargeting · demanda nueva. En lead gen sano parte en 70/20/10;
  en escalado se mueve hacia 50/20/30.
- **Por plataforma**: Google trabaja intención (se escribe para quien ya busca); Meta trabaja interrupción
  (la creatividad es la segmentación). No se recicla la misma pieza sin traducirla.
- **Por función del mensaje**: oferta · objeción · prueba · educación · identidad · urgencia real.
  Un mes con seis piezas de oferta y ninguna de objeción explica por qué el CPL no baja.

### 4. Ángulos — de dónde salen

Los ángulos se derivan de la ficha, no del catálogo de ideas: **una objeción real, una frase textual del
cliente, un diferencial verificable o un aprendizaje del mes anterior**. `references/angulos.md` tiene el
banco por vertical y las combinaciones que funcionan — se usa para ampliar, nunca para reemplazar la ficha.

Regla: **cada ángulo declara qué objeción ataca y con qué prueba la resuelve.** Si no tiene prueba, se
propone producir la prueba (testimonio, dato, caso) antes que el anuncio.

### 5. Volumen — cuántas piezas de verdad se necesitan

Ver `references/volumen-y-formatos.md`. Resumen: Meta necesita volumen y diversidad real (la creatividad
es la palanca desde Andromeda), Google necesita cobertura de assets completa por campaña. Planificar
menos piezas de las que la plataforma consume es la causa más común de fatiga a mitad de mes.

### 6. Calendario

Fechas de: brief → producción → aprobación del cliente → carga → activación → lectura de resultados.
El calendario incluye la **rotación programada** (qué se apaga y cuándo), no solo lo que se enciende.

### 7. Entrega

Formato completo en `references/plantillas.md`: plan del mes + tabla de piezas + briefs individuales +
qué se testea + criterio de éxito + qué se necesita del cliente y para cuándo.

---

## Cómo cierras siempre

- **3 prioridades del mes**, no diez.
- Cada pieza con su ángulo, su objeción, su formato, su plataforma y su fecha.
- Lo que se apaga, no solo lo que se enciende.
- Lo que necesitas del cliente, con fecha límite (sin fotos no hay pauta).
- El siguiente punto de control.

Para convertir cada línea del plan en un anuncio concreto — concepto, hook, guion, copy y specs — usa el
skill `ad-concepts`. Para definir cómo se comparan entre sí, usa `creative-testing`.
