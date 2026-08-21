# Escalado: reglas, orden y árbol de decisión

Todo se **propone**; el usuario ejecuta. Cada propuesta lleva métrica de control, fecha de revisión y rollback.

## Reglas duras

| Palanca | Paso máximo | Estabilización antes del siguiente paso |
|---|---|---|
| Presupuesto — Meta | +15–20% | 48–72 h |
| Presupuesto — Google | +20% | 7–14 días |
| Objetivo (tCPA/tROAS/coste por resultado) | ±10–15% | 7–14 días |
| Geografía o mercado nuevo | 1 por vez | 14 días |
| Formato/campaña nueva (PMax, Demand Gen, Advantage+) | 1 por vez, 10–20% del presupuesto | 4–6 semanas antes de juzgar |

- Cambios de presupuesto de ~30% o más reinician el aprendizaje en ambas plataformas.
- Nunca presupuesto y objetivo en el mismo movimiento: dos variables a la vez no son atribuibles.
- Volumen mínimo: Google ~30 conv/30 días (tCPA) y ~50 (tROAS); Meta ~50 eventos de optimización por
  conjunto por semana. Debajo de eso, **consolidar** antes que segmentar.
- Durante el aprendizaje el CPA corre 20–40% por encima del estado estable: no se juzga ahí.
- Si algo se rompe al escalar: **volver al último escalón estable**, no seguir aflojando el objetivo.

## Orden de escalado (no saltarse pasos)

1. **Destrabar lo rentable** que esté limitado por presupuesto. El escalado más barato que existe.
2. **Ampliar cobertura** de lo que ya funciona: más intención (Google) o más públicos/creatividad de los ángulos ganadores (Meta).
3. **Ampliar geografía o catálogo**.
4. **Aflojar el objetivo** de forma escalonada para comprar volumen adicional.
5. **Sumar formato o canal**: PMax/Demand Gen en Google; Advantage+ o placements nuevos en Meta.
6. **Ampliar la oferta**: proyectos, categorías, ángulos, promociones.

Cuando lo que falta es demanda y no presupuesto, los pasos 1–4 dejan de rendir: ahí entra generación de
demanda y el crecimiento se mide con **incrementalidad**, no con atribución de último clic.

## Árbol de decisión mensual

```
¿CPA/CPL/ROAS dentro del objetivo (±15%) en los últimos 30 días?
├── SÍ  → ¿Está limitada por presupuesto?
│         ├── SÍ  → proponer +20% (Google) / +15–20% (Meta); revisar en 7–14 días / 48–72 h
│         └── NO  → aflojar objetivo 10%  O  ampliar cobertura/geo  O  sumar formato
└── NO  → identificar el cuello de botella antes de tocar nada:
          ├── Señal      → conversión primaria, CAPI/EC, EMQ, valor real, consolidar campañas
          ├── Tráfico    → negativos y exclusiones (Google) · públicos y solapamiento (Meta) · geo, horario
          ├── Creatividad→ fatiga, poca diversidad de ángulos, formatos faltantes (causa nº1 en Meta)
          ├── Landing / producto → CRO, velocidad, precio, stock. NO más presupuesto
          └── Comercial / operación → SLA de contacto, logística, inventario. Se documenta, no se compensa
```

## Guardarraíles antes de cada paso

- [ ] ¿Se mantiene la **calidad** (leads calificados / margen), o solo bajó el costo bruto?
- [ ] ¿El crecimiento viene de marca o retargeting? Entonces no es crecimiento, es cosecha.
- [ ] ¿Aguanta la operación el volumen extra (equipo comercial, stock, despacho)?
- [ ] ¿Hay creatividad suficiente para sostener más gasto sin disparar frecuencia?
- [ ] ¿Está escrito el paso con métrica de control, fecha de revisión y condición de rollback?
