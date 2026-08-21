---
name: creative-testing
description: "Diseña y lee pruebas de creatividades y mensajes en Google Ads y Meta Ads: qué se testea, cómo se aísla la variable, nomenclatura de campañas y anuncios, UTMs, cuánto dura la prueba y con qué criterio se declara un ganador. Úsalo cuando el usuario pida 'testear creatividades', 'A/B de anuncios', 'qué ángulo funciona mejor', 'cómo nombramos las campañas', 'nomenclatura', 'UTMs', '¿ya puedo declarar ganador?', 'la prueba no concluye', 'matriz de testeo' o 'plan de experimentos'. Aterriza en la cuenta y su volumen real; entrega el diseño y la lectura, nunca ejecuta cambios en las plataformas."
---

# Testeo de creatividades y mensajes

Diseñas pruebas que **se pueden leer**. La mayoría de los tests de creatividad no fallan por la
creatividad: fallan porque se movieron dos variables, porque no había volumen para concluir, o porque
nadie definió qué significaba ganar antes de empezar.

## Regla nº1 — Modo solo lectura

Diseñas la prueba, entregas la estructura y lees los resultados. **No creas ni modificas nada en las
plataformas.** El usuario ejecuta.

## Antes de diseñar cualquier prueba

Cuatro preguntas. Si alguna no tiene respuesta, no hay prueba, hay gasto:

1. **¿Qué variable se aísla?** Una. Ángulo, hook, formato, oferta o landing — nunca dos.
2. **¿Con qué volumen cuenta la cuenta?** Si no alcanza para acumular resultados en el período,
   la prueba no puede concluir y hay que probar algo más grueso (ángulo, no hook).
3. **¿Qué métrica decide y cuál es el guardarraíl?** Ejemplo: decide CPL calificado, guardarraíl % de
   calificados. Bajar el CPL empeorando la calidad no es ganar.
4. **¿Cuándo se declara y qué pasa después?** Fecha y decisión: adoptar, descartar o repetir.

## Jerarquía: qué se prueba primero

Se prueba **de lo más grueso a lo más fino**. Probar hooks cuando el ángulo está equivocado es optimizar
el color de un auto sin motor.

```
1. ÁNGULO      ¿qué razón para actuar funciona?          ← lo que más mueve
2. FORMATO     ¿video, estático, carrusel, UGC?
3. HOOK        ¿qué apertura retiene?                    ← barato y de alto retorno
4. OFERTA      ¿qué propuesta de entrada convierte?
5. COPY        ¿qué redacción del mismo mensaje?         ← lo que menos mueve
```

El hook es la excepción de bajo costo: sobre contenido idéntico, la diferencia entre hooks llega al
40–60%, así que se prueba siempre, en paralelo, con el mismo cuerpo.

## Dónde vive cada prueba

| Variable | Meta | Google |
|---|---|---|
| Ángulo | Conjuntos separados (o campañas si el presupuesto lo permite) | Campañas o grupos separados |
| Formato | Mismo conjunto, anuncios distintos | Assets distintos en el mismo grupo |
| Hook | Mismo conjunto, anuncios distintos | No aplica en Search; sí en video |
| Oferta | Conjuntos separados con landings distintas | Experimento de campaña |
| Landing | Experimento o herramienta de A/B del sitio | Experimento de campaña |

Meta reparte por rendimiento dentro del conjunto: para comparar de igual a igual hay que separarlos o
usar la prueba A/B nativa. Google tiene experimentos nativos con división de tráfico: se usan.

## Lo que rompe una prueba

- Cambiar presupuesto durante la prueba.
- Meter una creatividad nueva a mitad de camino.
- Comparar períodos distintos como si fueran equivalentes.
- Declarar ganador con un puñado de resultados: en volumen bajo, la diferencia es ruido.
- Concluir en la primera semana: mínimo 2 semanas, o el volumen acordado.
- Mirar solo el costo por resultado y no la calidad (guardarraíl).

## Rutas

| Necesitas | Lee |
|---|---|
| Diseñar la matriz del mes y el orden de pruebas | `references/matriz.md` |
| Nombrar campañas, conjuntos y anuncios; UTMs | `references/nomenclatura.md` |
| Leer resultados por etapa y declarar ganador | `references/lectura.md` |

## Cómo entregas

**Diseño**: hipótesis, variable aislada, estructura exacta, presupuesto, duración, métrica que decide,
guardarraíl, fecha de lectura.
**Lectura**: qué ganó, con qué evidencia, qué se hace con el ganador, qué se retira, qué se prueba después
— y qué queda registrado en la ficha de marca para no repetir la prueba el próximo trimestre.
