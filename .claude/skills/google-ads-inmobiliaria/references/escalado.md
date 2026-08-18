# Escalado: reglas, orden y árbol de decisión

## Reglas duras

| Palanca | Paso máximo | Espera antes del siguiente paso |
|---|---|---|
| Presupuesto diario | **+20%** | 7–14 días |
| tCPA / tROAS | **±10–15%** | 7–14 días |
| Geografía nueva | 1 mercado por vez | 14 días |
| Formato nuevo (PMax, Demand Gen) | 1 por vez, presupuesto de prueba 10–20% | 4–6 semanas antes de juzgar |

- Cambios de presupuesto de **~30% o más pueden reiniciar el aprendizaje**.
- Cualquier cambio de objetivo inicia una nueva fase de aprendizaje: no cambiar presupuesto y objetivo
  en la misma semana.
- **No tocar nada durante el aprendizaje** (~7 días o ~30 conversiones desde el último cambio estructural).
- Volumen mínimo para automatizar: **~30 conversiones/30 días (tCPA)**, **~50 (tROAS)**. Debajo de eso,
  **consolidar** campañas en lugar de segmentar más.
- **PMax: 6 semanas** antes de cambios mayores.
- Si el rendimiento se rompe al escalar: **volver al último escalón estable**. No compensar bajando el
  objetivo mientras se sube presupuesto (se rompen las dos variables a la vez).

## Orden de escalado (no saltarse pasos)

1. **Destrabar lo rentable**: subir presupuesto donde la campaña esté "limitada por presupuesto" y el
   CPA/ROAS esté en objetivo. Es el escalado más barato que existe.
2. **Ampliar intención**: más keywords/temas de búsqueda de la misma familia que ya convierte.
3. **Ampliar geografía**: comunas/ciudades vecinas; nacional para producto de inversión.
4. **Aflojar el objetivo** escalonadamente (tCPA +10% / tROAS -10%) para comprar volumen adicional.
5. **Sumar formato**: PMax con señales de calidad, luego Demand Gen/YouTube para demanda nueva.
6. **Ampliar oferta**: nuevos proyectos, nuevas categorías, nuevos ángulos de landing.

Cuando lo que falta es demanda (no presupuesto), los pasos 1–4 ya no rinden: ahí entra Fase 4
(generación de demanda) y el crecimiento se mide con incrementalidad, no con CPA de última interacción.

## Árbol de decisión mensual

```
¿CPA/ROAS dentro del objetivo (±15%) en los últimos 30 días?
├── SÍ  → ¿La campaña está limitada por presupuesto?
│         ├── SÍ  → +20% de presupuesto; revisar en 7–14 días
│         └── NO  → aflojar objetivo 10%  O  ampliar intención/geo  O  sumar formato
└── NO  → identificar el cuello de botella:
          ├── Señal (pocas conversiones, aprendizaje eterno)
          │     → consolidar campañas, valor por etapa, enhanced conversions, bajar segmentación
          ├── Calidad de tráfico (muchos clics, leads basura)
          │     → negativos, exclusiones de marca, revisar canales de PMax, geo, horario, dispositivo
          ├── Landing (buen CTR, mala CVR)
          │     → CRO: formulario, headline, velocidad, prueba social. NO más presupuesto
          └── Comercial (leads calificados que nadie contacta)
                → SLA ≤5 min, guion, seguimiento. Documentar y comunicar; NO subir presupuesto
```

## Cambio del 17 de agosto de 2026 (revisar antes de fijar objetivos)

Las campañas **limitadas por presupuesto** con tCPA/tROAS ya no buscan superar el objetivo: apuntan al
número exacto configurado. Consecuencia práctica: si tu tCPA estaba puesto "holgado" porque el algoritmo
rendía mejor que él, tu CPA real va a subir hacia ese número.

Acción: **realinear los objetivos al rendimiento real de los últimos 30 días** (no al deseado), y solo
después decidir si se escala. Alternativas transitorias: pasar a `Maximizar conversiones` si se prioriza
volumen, o subir presupuesto si el ROI ya es bueno y ahora el sistema es más predecible.

## Guardarraíles de escalado (revisar en cada paso)

- [ ] ¿Está estable el % de leads calificados, o solo bajó el CPL bruto? (escalar volumen basura es retroceder)
- [ ] ¿Subió la participación de **marca** en las conversiones? Si el crecimiento es solo marca, no hay crecimiento.
- [ ] ¿Aguanta el equipo comercial el volumen nuevo con SLA ≤5 min?
- [ ] ¿Hay inventario/stock (ecommerce) o unidades disponibles (inmobiliaria) para el volumen extra?
- [ ] ¿Está registrado el paso en el log con fecha de revisión y condición de rollback?
