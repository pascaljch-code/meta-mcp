# Matriz de testeo mensual

## Cómo se arma

Del plan del mes salen los ángulos; de la matriz sale cómo se comparan.

```
| # | Hipótesis | Variable aislada | Estructura | Presupuesto | Métrica | Guardarraíl | Lee el |
|---|-----------|------------------|------------|-------------|---------|-------------|--------|
```

La hipótesis se escribe completa: **"si [cambio], entonces [efecto] porque [razón]"**. Sin el "porque"
no hay aprendizaje: solo un resultado que no se puede extrapolar.

## Cuántas pruebas por mes

Depende del volumen, no del entusiasmo:

| Volumen mensual de conversiones | Pruebas simultáneas | Qué se prueba |
|---|---|---|
| < 30 | 1 | Solo ángulo. Nada más tiene con qué concluir |
| 30–100 | 1 gruesa + hooks en paralelo | Ángulo + variantes de hook del ganador anterior |
| 100–300 | 2 | Ángulo + formato u oferta |
| > 300 | 3 | Ángulo, formato y landing |

Los hooks son la excepción: se pueden correr en paralelo siempre, porque comparten cuerpo y se leen con
métricas tempranas (retención inicial), que acumulan mucho más rápido que las conversiones.

## Cadencia estándar

- **Semana 1**: lanzamiento con presupuesto parejo. No se toca nada.
- **Semana 2**: primera lectura de métricas tempranas (retención, CTR). Se puede apagar lo evidentemente
  muerto; no se declara ganador.
- **Semanas 3–4**: lectura de métricas de resultado. Se declara, se documenta y se explota el ganador.

## El presupuesto de exploración

Un porcentaje fijo del mes va a probar cosas nuevas, y se defiende de la tentación de apagarlo cuando
el mes viene apretado:

| Fase de la cuenta | Exploración |
|---|---|
| 1–2 (captura, calidad) | 20–30% — hay que encontrar qué funciona |
| 3 (escalado) | 15–20% — sostener el pipeline de ganadores |
| 5 (régimen) | 10–15% — evitar la fatiga estructural |

Sin presupuesto de exploración, la cuenta vive de un ganador hasta que se fatiga, y ahí no hay reemplazo
listo. Ese es el patrón que hace caer cuentas que venían bien.

## Explotar al ganador

Cuando un ángulo gana, el mes siguiente **no se busca otro ángulo**: se producen variantes del que ganó
(3 hooks nuevos, otro formato, otra voz, otra prueba, otro nivel de conciencia) y se prueba **un solo**
ángulo nuevo. Asumir que 12–18% de las creatividades escala significa que un ganador vale más explotado
que reemplazado.
