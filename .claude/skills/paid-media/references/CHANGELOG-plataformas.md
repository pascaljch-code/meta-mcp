# Changelog de plataformas

Registro fechado de cambios que **modifican la operación**. Se actualiza con `../ACTUALIZACION.md`.
Formato: fecha · qué cambió · qué hacemos distinto · fuente. Lo más nuevo arriba.
Un hallazgo que no cambia ninguna acción no se registra: esto no es un feed de noticias.

---

## Revisado el 2026-08-18 (siembra inicial)

### GOOGLE ADS

**2026-08-17 · Smart Bidding deja de superar el objetivo en campañas limitadas por presupuesto**
Con tCPA/tROAS, las campañas limitadas por presupuesto apuntan al número exacto configurado en vez de
buscar rendimiento mejor. Los CPA reales pueden subir hacia el objetivo.
*Operación:* realinear objetivos al rendimiento real de 30 días antes de escalar; transitoriamente,
`Maximizar conversiones` si se prioriza volumen.
https://www.dolnai.com/posts-es/importante-cambio-en-smart-bidding-17-agosto-de-2026

**2026-06-15 · Subidas de conversiones migran a la Data Manager API**
Offline conversion import y enhanced conversions for leads quedan bloqueados en la Google Ads API.
*Operación:* no construir integraciones nuevas sobre la Ads API; preferir enhanced conversions for leads.
https://support.google.com/google-ads/answer/14274408

**2026-06 · Enhanced conversions de web y leads se unifican** en un solo interruptor.
*Operación:* revisar configuración para no duplicar eventos.

**2026-06-03 · Demand Gen/Discovery restringidos en categorías sensibles**
Usan audiencias curadas por el anunciante por defecto y pueden quedar limitadas de entregar.
*Operación:* en vivienda US/CA, no depender de audiencias propias; intención y geo.
https://support.google.com/adspolicy/answer/143465

**2026 · Controles de PMax ampliados**
10.000 negativos por campaña y negativos de cuenta · 25 temas de búsqueda por grupo de assets ·
exclusiones de marca · exclusión de públicos 1P · reporte por canal y de términos · 15 videos por grupo ·
A/B de asset sets.
*Operación:* el control semanal de PMax pasa a obligatorio.
https://business.google.com/en-all/accelerate/resources/articles/new-performance-max-steering-and-reporting-updates-coming-in-2026/

**2026 · Search sigue por delante de PMax en calidad de lead** (25–45% mejor en costo por lead calificado
en servicios y B2B, según datos independientes).
*Operación:* Search como motor en lead gen; PMax como complemento con señal de calidad.

### META ADS

**2025-10 · Andromeda completó su despliegue global**
El motor de recuperación de anuncios selecciona audiencia a partir de la creatividad.
*Operación:* la palanca principal pasa de segmentación a **volumen y diversidad creativa** (15–50+ activas);
consolidar conjuntos y multiplicar ángulos y formatos.

**2026 · Ajuste de atribución**
La columna por defecto separa clics en enlace de acciones sociales e incorpora engage-through de 1 día.
*Operación:* advertir el cambio en cualquier comparación año contra año; contrastar con backoffice.

**2026 · Opportunity Score disponible para todos los anunciantes**
Mide adherencia a las prácticas recomendadas de Meta, **no** rendimiento.
*Operación:* usarlo como checklist de configuración; rechazar sugerencias que rompan la lectura de
incrementalidad o la separación prospecting/retargeting.

**2026 · HEC ampliado en Meta**
Mayor alcance y fiscalización de la categoría especial (vivienda, empleo, crédito).
*Operación:* verificar marcado de categoría en toda cuenta inmobiliaria con tráfico US/CA.

### VIGENTES (verificados 2026-08-18)

- Google: ~30 conversiones/30 días para tCPA, ~50 para tROAS · ventana de 63 días para conversiones offline
  · cambios de presupuesto ≥~30% pueden reiniciar el aprendizaje · PMax necesita ~6 semanas.
- Meta: ~50 eventos de optimización por conjunto por semana para salir de aprendizaje · durante el
  aprendizaje el CPA corre 20–40% por encima del estado estable · subir presupuesto 15–20% cada 48–72 h.
- Meta: píxel + CAPI deduplicados es el mínimo, no una mejora; vigilar EMQ del evento principal.
- Formulario ideal en lead gen: 3–5 campos; cada campo extra resta 5–10% de conversión, pero las preguntas
  calificadoras mejoran la calidad.
