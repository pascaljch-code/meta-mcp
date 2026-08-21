# Google Ads — especificidades

## Qué mirar y en qué orden (semanal)

1. **Términos de búsqueda** (Search, PMax y AI Max, 7–14 días): candidatos a negativo por irrelevancia
   *y por mala calidad de resultado*; candidatos a keyword propia entre los que convierten.
2. **Objetivos de puja** vs. rendimiento real de 14 días.
3. **PMax**: reporte por canal ("Dónde se mostraron los anuncios"), temas de búsqueda, exclusiones de
   marca, rendimiento de assets por grupo.
4. **RSA**: calificación de assets, cobertura de intención, concordancias y canibalización entre ad groups.
5. **Cobertura**: cuota de impresiones perdida por presupuesto vs. por ranking — dicen cosas distintas.

## Estructura

- **Marca siempre separada** de genérico, y medida aparte. Si el crecimiento del mes vino de marca, no hubo crecimiento.
- Un ad group por **intención cerrada** (agrupar variantes de la misma intención; no SKAG extremo).
- Una landing por intención; nunca al home.
- Remarketing/RLSA activo.
- **PMax entra después** de tener señal de conversión de calidad. Antes canibaliza marca y reporta ROAS ficticio.
- Ubicación configurada por **presencia**, no por interés, salvo caso justificado.

## Automatización: qué controlar

| Control | Estado actual | Uso |
|---|---|---|
| Negativos en PMax | hasta 10.000 por campaña + nivel de cuenta | Revisión semanal obligatoria |
| Temas de búsqueda | hasta 25 por grupo de assets | Dirigir a qué consultas priorizar |
| Exclusiones de marca | nivel campaña | Marca propia y competidores |
| Exclusión de públicos 1P | disponible | Excluir clientes actuales o listas de baja calidad |
| Reporte por canal y de términos | disponible | Detectar fuga a Display/YouTube sin resultado |
| Video en grupo de assets | hasta 15 | Subir propio: el autogenerado suele desviar el mensaje |
| A/B de asset sets | disponible | Probar creatividad con control/tratamiento |

## Pujas

- Arranque sin historial: `Maximizar conversiones` sin objetivo 2–3 semanas → luego tCPA con el **CPA real**.
- Con valor confiable (margen o etapas de CRM): `Maximizar valor` + tROAS.
- **Desde el 17-ago-2026** las campañas limitadas por presupuesto con tCPA/tROAS ya no rinden mejor que el
  objetivo: apuntan al número exacto. Los objetivos "holgados" ahora encarecen el CPA real → realinear al
  rendimiento real de 30 días antes de escalar.
- tCPA necesita ~30 conversiones/30 días; tROAS ~50.

## Search vs. PMax para lead gen

Los datos independientes de 2026 siguen mostrando **Search por delante de PMax en costo por lead
calificado** en servicios y B2B (rango reportado 25–45%). Search (con AI Max cuando aplique) como motor;
PMax como complemento una vez que existe señal de calidad.

## Extracción mínima para un diagnóstico

Campaña · tipo · estrategia de puja y objetivo · presupuesto y si está limitado · gasto, conversiones,
CPA, valor y ROAS (7/28/90 días) · cuota de impresiones perdida por presupuesto y por ranking ·
% de conversiones de marca · estado de aprendizaje · conversiones activas y cuál es primaria.
