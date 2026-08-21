---
name: cierre-mensual
description: "Cierra el mes de una cuenta publicitaria: extrae el rendimiento real de Google Ads y Meta Ads, lo compara con la línea base y el objetivo, nombra el cuello de botella, actualiza la ficha de la cuenta y arma el reporte del cliente con las propuestas del mes siguiente. Úsalo cuando el usuario pida 'cerrar el mes', 'reporte mensual', 'informe del cliente', 'cómo nos fue en [mes]', 'resumen de resultados', 'actualizar la ficha' o 'qué proponemos para el mes que viene'. Modo solo lectura: extrae, analiza y propone; nunca ejecuta cambios en las cuentas."
---

# Cierre mensual de cuenta

Conviertes un mes de datos en tres cosas: **un veredicto** (qué pasó y por qué), **una ficha actualizada**
(para que el mes siguiente no parta de cero) y **un reporte que el cliente entiende**.

## Regla nº1 — Modo solo lectura

Extraes, analizas, propones. **Nunca ejecutas cambios en las cuentas.** Las propuestas van con la ruta
exacta para que el usuario las aplique.

## Regla nº2 — Un cierre sin veredicto no es un cierre

Una tabla de métricas no es un reporte. El cierre debe responder, en una frase que el cliente pueda
repetir: **qué limitó el resultado este mes**. Si no puedes nombrarlo, no terminaste el análisis.

---

## Proceso

### 1. Extraer (mes cerrado, mismo período en ambas plataformas)

**Transversal**: inversión · resultados · costo por resultado · valor · tendencia semana a semana ·
comparación con mes anterior y con el mismo mes del año pasado si existe.

**Google**: por campaña y tipo · estrategia y objetivo vigente · cuota de impresiones perdida por
presupuesto y por ranking · % de conversiones de marca vs. no marca · términos nuevos relevantes.

**Meta**: por campaña y conjunto · prospecting vs. retargeting · frecuencia y CPM · concentración de gasto
por creatividad · estado de aprendizaje · EMQ del evento principal.

**Fuera de plataforma** (el dato que hace la diferencia): CRM con etapas y % de calificados (lead gen), o
backoffice con margen, devoluciones y clientes nuevos (ecommerce). Sin esto, el cierre habla de costo por
formulario, no de negocio.

### 2. Contrastar

Contra **línea base y objetivo de la ficha**, nunca contra benchmarks externos. Y contra la propia
tendencia: un mes bueno dentro de una caída de tres meses no es un mes bueno.

Verificar antes de concluir: ¿hubo cambio de atribución, de tracking, de estacionalidad o de precio que
explique el movimiento sin que nadie haya hecho nada?

### 3. Nombrar el cuello de botella

Uno, el principal: **señal · tráfico o segmentación · creatividad · landing o producto · comercial u
operación**. Con la evidencia que lo sostiene y qué lo confirmaría o descartaría.

Si es del cliente (leads sin contactar, quiebres de stock, demoras de despacho), se dice con datos y sin
rodeos. Callarlo por incomodidad hace que el mes siguiente se repita y que la culpa recaiga en la cuenta.

### 4. Actualizar la ficha

Es el paso que la mayoría se salta y el que hace que el sistema mejore con el tiempo:

- Fase vigente y criterio de salida pendiente
- Línea base con los números del mes cerrado
- Estado de la señal (qué se arregló, qué falta)
- **Registro de ángulos**: qué se probó, qué ganó, qué murió y por qué
- Guardarraíles que cambiaron (presupuesto, capacidad operativa, estacionalidad)

### 5. Proponer el mes siguiente

3 prioridades, no diez. Propuestas en formato P1/P2/P3 con hallazgo → evidencia → propuesta → dónde
aplicarlo → riesgo → métrica → rollback. Presupuesto sugerido con su justificación y lo que se espera
que ocurra.

La decisión de escalar sale del árbol de decisión de `paid-media`, no del ánimo del mes.

### 6. Reporte

Formato en `references/reporte.md`. Dos versiones: la interna (todo) y la del cliente (media plana con
lo que necesita para decidir).

---

## Encadenamiento

Este cierre alimenta el mes siguiente: el cuello de botella define el objetivo de la pauta de contenidos,
el registro de ángulos define qué se explota y qué no se vuelve a probar, y la fase actualizada define
las reglas de escalado que aplican.

`cierre-mensual` → `pauta-contenidos` → `ad-concepts` → `creative-testing` → `cierre-mensual`.
