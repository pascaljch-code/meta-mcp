# Señal y tracking — la base de todo

Sin esto, cualquier análisis es adivinanza. Es lo primero que se audita en una cuenta nueva o heredada.

## Mínimo por objetivo

| Pieza | Lead gen | Ecommerce / retail |
|---|---|---|
| Conversión primaria | **Lead calificado** (etapa de CRM) | Compra con valor real |
| Secundarias (observación) | Formulario, llamada >60s, WhatsApp, agendamiento | Add to cart, inicio de checkout |
| Google | Enhanced conversions (web y leads) | Enhanced conversions + Merchant Center |
| Meta | Píxel + CAPI deduplicados; EMQ vigilado | Píxel + CAPI + catálogo al día |
| Consentimiento | Consent Mode v2 con tráfico EEA/UK; estado en cada subida | Igual |
| Identificador de clic | GCLID/GBRAID/WBRAID y fbclid guardados en el CRM | order_id + identificadores de clic |
| Valor | Índice por etapa del embudo | Margen de contribución, no ingreso bruto |

**Una sola conversión primaria por objetivo.** Varias primarias hacen que el sistema optimice al promedio
de cosas que no valen lo mismo — causa nº1 de "muchos resultados, cero negocio".

## Google — importación de valor real

- Camino recomendado hoy: **enhanced conversions for leads** (identificadores hasheados) antes que el
  offline conversion import clásico basado solo en GCLID.
- **Si el CRM no guarda el identificador de clic, no hay importación offline.** Campo oculto en el
  formulario + persistencia del parámetro en cookie de primera parte.
- **Ventana de 63 días** desde el último clic: define en qué etapa puede estar la conversión primaria
  en ciclos largos.
- Las subidas migran a la **Data Manager API** y quedan bloqueadas en la Google Ads API: no construir
  integraciones nuevas sobre la Ads API.
- Toda subida debe llevar el estado de consentimiento (`ad_user_data`, `ad_personalization`); sin
  `granted`, los datos hasheados se descartan del lado del servidor.

## Meta — calidad de coincidencia

- Píxel y CAPI en paralelo **con deduplicación por event_id**; sin deduplicar, se infla el reporte.
- **EMQ por evento**: subir enviando email, teléfono, IP, user agent, fbc/fbp y external_id, con
  consentimiento. Un EMQ bajo en el evento de compra se ve como "Meta no encuentra compradores".
- Para lead gen con CRM: subir conversiones offline con el estado real del lead cierra el círculo igual
  que en Google.

## Escala de valor para lead gen (índice, no dinero real)

| Etapa CRM | Conversión | Valor índice |
|---|---|---|
| Formulario enviado | Lead | 1 |
| Contactado | Lead contactado | 5 |
| Calificado | **Lead calificado** ← primaria | 25 |
| Reunión / visita agendada | Agendado | 60 |
| Reunión / visita realizada | Realizado | 120 |
| Propuesta aceptada / reserva | Reserva | 600 |
| Venta cerrada | Venta | 3000 |

Los valores reflejan la probabilidad real de cierre de cada etapa; se recalibran cada trimestre.
Usar índice y no dinero evita exponer información comercial y permite comparar productos de distinto ticket.

## Valor en ecommerce

- Valor de conversión = **margen de contribución** (sin impuestos, envío ni devoluciones sistemáticas).
- Categorías con alta devolución (fashion/tallas) deben corregir el valor o el ROAS miente por diseño.
- Distinguir **cliente nuevo vs. recurrente**: el ROAS de cliente nuevo es la métrica de crecimiento;
  el mezclado premia el retargeting.

## Auditoría rápida de datos (mensual)

- [ ] Conversión primaria única, sin duplicados ni dobles tags.
- [ ] Diferencia plataforma vs. backoffice/CRM <10% en volumen; si es mayor, hay pérdida de señal.
- [ ] % de registros con identificador de clic capturado >90%.
- [ ] Enhanced conversions grabando; EMQ aceptable en el evento principal.
- [ ] Consent: el banner no bloquea el tag antes del consentimiento y el modelado funciona.
- [ ] Ventana de conversión coherente con el ciclo de compra real.
- [ ] Ecommerce: catálogo/feed con precio, stock y disponibilidad al día.
