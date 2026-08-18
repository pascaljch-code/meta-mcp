# Estructura de cuenta y fases de madurez

## Fases (se avanza por criterio cumplido, no por calendario)

| Fase | Objetivo | Criterio de salida |
|---|---|---|
| 0. Cimientos (días 1–10) | Cuenta medible y limpia | Test end-to-end clic→lead→CRM→conversión importada, línea base de 90 días documentada |
| 1. Captura de demanda (sem. 2–5) | Comprar la demanda existente | ≥30 conversiones primarias/30 días por campaña con tCPA (≥50 si irá a tROAS) |
| 2. Calidad y valor (sem. 5–9) | Que el algoritmo compre el lead que cierra | ≥30 "lead calificado"/30 días y % calificados estable o al alza 3 semanas |
| 3. Escalado (sem. 9–20) | Más inversión sin perder eficiencia | +50% inversión vs. línea base con CPA/ROAS en ±15% del objetivo |
| 4. Generación de demanda (mes 5+) | Llenar el embudo alto | Demand Gen/YouTube con CPL calificado aceptable y prueba de incrementalidad |
| 5. Régimen | Defender la eficiencia | Continuo |

## Fase 0 — checklist de cimientos

- Una sola conversión primaria; el resto en "secundaria (observación)".
- Enhanced conversions activas; Consent Mode v2 si hay tráfico EEA/UK.
- GA4 y Merchant Center vinculados (ecommerce).
- Marca separada de genérico. Exclusiones de marca en PMax.
- Listas de negativos de cuenta: empleo/trabajo, "gratis", DIY, competidores no deseados,
  intenciones ajenas ("arriendo" si solo se vende, "planos", "tesis", "curso").
- Landing por intención, formulario 3–5 campos + 1–2 preguntas calificadoras, thank-you page medida.
- CRM con GCLID/GBRAID/WBRAID, etapa y valor. SLA de primer contacto ≤5 min.

## Estructura — inmobiliaria (lead gen)

Segmentar por **intención de búsqueda**, no por producto. Cuatro ejes que funcionan:

1. **Marca** — nombre de la inmobiliaria y de los proyectos. Barato, defensivo, se mide aparte.
2. **Proyecto + Ubicación** — "departamentos [proyecto]", "[proyecto] precios".
3. **Categoría + Ubicación** — "departamentos nuevos [comuna]", "casas en venta [ciudad]".
   El eje de mayor volumen y donde se gana o se pierde la cuenta.
4. **Intención financiera / inversión** — "subsidio", "crédito hipotecario", "invertir en departamento",
   "arriendo garantizado". Lead distinto, landing distinta, valor distinto.

Reglas:
- 1 landing por intención; nunca al home.
- Un ad group por intención cerrada (no SKAG extremo: agrupa variantes de la misma intención).
- Remarketing siempre activo (reduce CPL ~20–40% en este vertical).
- PMax solo cuando ya hay historial de conversiones **de calidad**; antes canibaliza marca.
- Geo: radio por comuna/ciudad para producto de residencia; nacional o multi-ciudad para inversión.
- Horario: si el equipo comercial no atiende de noche/fin de semana, ajusta programación o acepta CPL mayor
  con SLA roto (peor negocio).

## Estructura — ecommerce

1. **Search marca** (defensa, presupuesto acotado).
2. **Search genérico por categoría** con intención comercial.
3. **Shopping / PMax con feed**: separar por margen o por rendimiento (top sellers vs. cola larga),
   con exclusiones de marca para que PMax no se coma la búsqueda de marca.
4. **Remarketing dinámico**.
5. **Demand Gen** para embudo alto una vez que PMax es estable: la dupla PMax + Demand Gen es la
   combinación con mejores resultados reportados (20–30% de mejora en ROAS) — pero exige feed impecable.

Feed = producto: títulos, descripciones, atributos e imágenes son la palanca de rendimiento nº1
antes de tocar cualquier puja.

## PMax y AI Max: controles que hoy existen y hay que usar

- **Temas de búsqueda**: hasta 25 por grupo de assets — dirigen a qué consultas priorizar.
- **Negativos**: hasta 10.000 por campaña + negativos a nivel de cuenta.
- **Exclusiones de marca** a nivel campaña (competidores y marca propia).
- **Exclusión de audiencias 1P** (ej. excluir clientes actuales o listas de baja calidad).
- **Reporte por canal** ("Dónde se mostraron los anuncios") y términos de búsqueda: úsalo semanalmente
  para detectar si el gasto se está fugando a Display/YouTube sin conversión útil.
- **Video**: hasta 15 por grupo de assets. Si no subes video, Google genera uno; en inmobiliaria
  suele convenir subir propio.
- **A/B en asset sets** para probar creatividad con control/tratamiento.

Elección de tipo de campaña para lead gen: **Search (con o sin AI Max) sigue dando leads de mejor calidad
que PMax** en servicios y B2B; PMax entra como complemento después de tener señal de calidad, no antes.
