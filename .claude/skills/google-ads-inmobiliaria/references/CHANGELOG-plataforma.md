# Changelog de plataforma y mejores prácticas

Registro fechado de cambios de Google Ads que **modifican la operación**. Se actualiza con la rutina de
`../ACTUALIZACION.md`. Formato: fecha del cambio · qué cambió · qué hacemos distinto · fuente.

Lo más nuevo arriba. Un hallazgo que no cambia nada en la operación no se registra aquí.

---

## Revisado el 2026-08-18 (siembra inicial)

### 2026-08-17 · Smart Bidding deja de superar el objetivo en campañas limitadas por presupuesto
Las campañas con tCPA/tROAS limitadas por presupuesto ya no buscan proactivamente rendir mejor que el
objetivo configurado: apuntan al número exacto. Los CPA reales pueden subir hacia el objetivo.
**Operación:** realinear tCPA/tROAS al rendimiento real de los últimos 30 días; alternativas transitorias:
`Maximizar conversiones` si se prioriza volumen, o subir presupuesto si el ROI ya es bueno.
Fuente: https://www.dolnai.com/posts-es/importante-cambio-en-smart-bidding-17-agosto-de-2026

### 2026-06-15 · Migración de subidas de conversiones a Data Manager API
Las subidas de offline conversion import y de enhanced conversions for leads se migran a la Data Manager
API y quedan bloqueadas en la Google Ads API. Consent Mode v2 obligatorio para anunciantes del EEE.
**Operación:** no construir integraciones nuevas sobre la Google Ads API para subir conversiones;
preferir enhanced conversions for leads sobre OCI clásico.
Fuente: https://support.google.com/google-ads/answer/14274408

### 2026-06 · Enhanced conversions de web y de leads se unifican
Pasan a ser una sola funcionalidad con un interruptor on/off.
**Operación:** revisar la configuración para no duplicar eventos al momento de la unificación.
Fuente: https://www.uniconsent.com/blog/google-ads-consent-mode-change-2026

### 2026-06-03 · Demand Gen / Discovery y categorías sensibles
Demand Gen y Discovery usan audiencias curadas por el anunciante por defecto y pueden quedar restringidas
de entregar cuando promocionan categorías de interés sensibles (incluye vivienda en EE.UU./Canadá).
**Operación:** en vivienda US/CA, no depender de audiencias propias en Demand Gen; apoyarse en intención y geo.
Fuente: https://support.google.com/adspolicy/answer/143465

### 2026-04 · Datos de usuario aceptados desde tag, Data Manager y API en paralelo
Ya no hay que elegir una única fuente de datos de usuario.
**Operación:** se puede complementar el tag con subidas de CRM sin canibalizar la señal; vigilar duplicados.

### 2026 · Controles de Performance Max ampliados
Negativos hasta 10.000 por campaña (antes 100) y a nivel de cuenta; hasta 25 temas de búsqueda por grupo de
assets; exclusiones de marca a nivel campaña; exclusión de audiencias 1P; reporte por canal y de términos de
búsqueda; hasta 15 videos por grupo de assets; A/B testing de asset sets.
**Operación:** el control semanal de PMax pasa a ser obligatorio (canal + términos + negativos), no opcional.
Fuentes: https://business.google.com/en-all/accelerate/resources/articles/new-performance-max-steering-and-reporting-updates-coming-in-2026/ ·
https://www.karooya.com/blog/why-negative-keywords-matter-more-than-ever-in-performance-max-campaigns/

### 2026 · Search/AI Max sigue superando a PMax en calidad de lead
Datos independientes de 2026 muestran Search por delante de PMax en costo por lead calificado en servicios
y B2B (rango reportado 25–45% mejor).
**Operación:** en inmobiliaria, Search (con AI Max cuando aplique) es el motor; PMax entra como complemento
después de tener señal de calidad.
Fuente: https://www.groas.com/post/google-ads-ai-max-search-2026-setup-performance-data-guide

### Vigentes (verificados 2026-08-18)
- Ventana de 63 días para importar conversiones offline asociadas al último clic.
- Volumen mínimo: ~30 conversiones/30 días para tCPA, ~50 para tROAS.
- Cambios de presupuesto ≥~30% pueden reiniciar el aprendizaje; escalar de a +20%.
- PMax: esperar ~6 semanas antes de cambios mayores.
- Formulario ideal: 3–5 campos; cada campo extra resta 5–10% de conversión, pero las preguntas
  calificadoras mejoran calidad.
