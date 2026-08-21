# Entregables — modo solo lectura

Todo lo que produce este skill es **información y propuestas**. La ejecución en las cuentas es del usuario.
Por eso cada propuesta debe poder aplicarse sin volver a preguntar nada.

## Formato de una propuesta (unidad básica)

```
[P1] Título corto de la propuesta            Plataforma · Campaña/Conjunto
Hallazgo    Qué está pasando, en una frase.
Evidencia   Métricas y período exactos que lo sustentan.
Propuesta   El cambio concreto (valor actual → valor propuesto).
Aplicar en  Ruta exacta: pantalla, sección, campo.
Riesgo      Qué se puede romper y cuánto tarda en verse.
Control     Métrica a vigilar y fecha de revisión.
Rollback    Cómo volver atrás y con qué criterio.
```

Prioridad: **P1** afecta gasto o señal hoy · **P2** mejora medible en el mes · **P3** higiene o experimento.
Máximo 3 P1 por entrega: una lista de veinte cambios no se ejecuta.

Nunca escribas "ya lo ajusté" ni "lo dejé pausado". Escribe "propongo bajarlo de X a Y".

## Reporte mensual

```
CUENTA: ______  MES: ____  PLATAFORMAS: ______  OBJETIVO: lead gen / ecommerce

1. RESULTADO (consolidado y por plataforma)
| Métrica | Mes actual | Mes anterior | Objetivo | Δ |
Lead gen:   inversión · leads · leads calificados · % calificados · CPL · CPL calificado · agendados · cierres
Ecommerce:  inversión · pedidos · ingresos · margen · ROAS · ROAS cliente nuevo · AOV · CVR

2. CUELLO DE BOTELLA DEL MES
   [ ] Señal  [ ] Tráfico/segmentación  [ ] Creatividad  [ ] Landing/producto  [ ] Comercial/operación
   Evidencia:

3. QUÉ CAMBIÓ EN EL MES (máx. 5, con efecto medido)

4. PROPUESTAS PARA EL MES SIGUIENTE (P1/P2/P3, formato de arriba)

5. PRESUPUESTO SUGERIDO
   Actual → propuesto (+__%) · justificación · qué se espera que pase

6. QUÉ NECESITAMOS DEL CLIENTE
   (SLA de contacto, creatividades, stock, precios, accesos, datos del CRM)
```

## Log de cambios

```
| Fecha | Cuenta | Plataforma | Campaña | Cambio propuesto | Aplicado por/cuándo | Hipótesis | Métrica | Revisar el | Resultado |
```

Como no ejecutamos, la columna **"aplicado"** es la que da trazabilidad: sin ella no se puede atribuir
ningún resultado a ninguna decisión.

## Brief de onboarding

```
NEGOCIO: producto · ticket promedio · margen o comisión · tasa de cierre · objetivo del trimestre · CPA/CPL máximo tolerable (derivado, no deseado)
EMBUDO: CRM o plataforma de ecommerce · SLA de contacto · criterio exacto de "lead calificado" · quién marca las etapas
TÉCNICO: accesos (solo lectura basta) · píxel/tag · CAPI · consent · catálogo/feed · landings por intención
RESTRICCIONES: países (¿EE.UU./Canadá? → categorías especiales) · marca · precios publicables · competidores que no se pujan
```

## Ficha de experimento

```
Hipótesis: si ______, entonces ______ porque ______
Tipo: experimento de plataforma · A/B de landing · prueba creativa · geo-holdout
Métrica primaria ______ · guardarraíl ______ · duración mínima 2 semanas o ___ conversiones
Resultado ______ · Decisión: adoptar / descartar / repetir
```

## Auditoría rápida (30 min, cuenta nueva o heredada)

- [ ] Conversión primaria única y correcta para el objetivo
- [ ] Google: enhanced conversions · Meta: píxel + CAPI deduplicados y EMQ del evento principal
- [ ] Consent configurado si aplica
- [ ] Marca separada (Google) · prospecting separado de retargeting (Meta)
- [ ] Negativos de cuenta y exclusiones de marca (Google) · solapamiento de públicos (Meta)
- [ ] Ubicación por presencia
- [ ] Landings por intención; formulario de 3–5 campos con 1–2 calificadoras
- [ ] Identificador de clic guardado en el CRM (>90%)
- [ ] Objetivos alineados al rendimiento real de 30 días
- [ ] Campañas/conjuntos bajo el mínimo de volumen → candidatos a consolidación
- [ ] Catálogo/feed al día (ecommerce)
