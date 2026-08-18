# Políticas, restricciones y riesgos

## Vivienda (HEC) en EE.UU. y Canadá — targeting restringido

Si el cliente promociona venta o arriendo de viviendas y opera en **EE.UU. o Canadá**:

- **No se puede segmentar** por edad, género, estado civil ni parentalidad.
- **No se puede usar segmentación por ZIP code**.
- Las **audiencias curadas por el anunciante** (Customer Match, segmentos propios, expansión de audiencia,
  lookalikes) entran en el lado restringido cuando la campaña promociona categorías sensibles;
  las audiencias predefinidas de Google sí están permitidas.
- Desde el **3 de junio de 2026**, Demand Gen y Discovery usan audiencias curadas por el anunciante por
  defecto y pueden verse **restringidas de entregar** en categorías de interés sensibles.

Implicancia operativa: en esos mercados la estrategia se apoya en **intención de búsqueda, geografía amplia
y creatividad**, no en audiencias demográficas. Marcar la categoría correctamente en la configuración de la
campaña para evitar suspensiones.

Fuera de EE.UU./Canadá estas restricciones específicas no aplican, pero conviene evitar segmentación
demográfica agresiva en vivienda: además del riesgo reputacional, suele rendir peor que la intención.

## Riesgos de PMax que hay que controlar activamente

- **Canibalización de marca**: sin exclusiones de marca, PMax cosecha conversiones que ya eran tuyas
  y reporta un ROAS ficticio.
- **Fuga a Display/YouTube**: revisar el reporte por canal cada semana.
- **Assets generados automáticamente**: en inmobiliaria pueden producir claims incorrectos
  (precios, disponibilidad). Desactivar o revisar lo generado.
- **Aprendizaje sin señal de calidad**: PMax con "formulario enviado" como objetivo produce volumen basura a escala.

## Otros riesgos frecuentes

- **Datos personales**: nunca subir datos sin base legal ni sin consentimiento registrado; las subidas
  requieren estado de consentimiento (`ad_user_data`, `ad_personalization`).
- **Promesas en anuncios**: precios, dividendos, subsidios y plazos deben coincidir con la landing;
  discrepancias generan desaprobaciones y reclamos.
- **Reportes con datos de cliente**: si se publican en la web (ej. Vercel), activar protección de despliegue;
  `noindex` no restringe el acceso de quien tenga el enlace.
- **Cuentas nuevas**: verificación de anunciante pendiente puede frenar la entrega; iniciarla el día 1.
