# Tracking, conversiones y valor — la base de todo

Sin esto, cualquier optimización es adivinanza y cualquier escalado es riesgo puro.

## 1. Arquitectura mínima

| Pieza | Inmobiliaria | Ecommerce |
|---|---|---|
| Conversión primaria | **Lead calificado** (etapa CRM) | Compra con valor real |
| Secundarias (observación) | Formulario, llamada >60s, WhatsApp, visita agendada | Add to cart, inicio checkout |
| Enhanced conversions | Web **y** leads | Web |
| Consent Mode v2 | Obligatorio con tráfico EEA/UK | Obligatorio con tráfico EEA/UK |
| ID de clic en CRM | GCLID, GBRAID, WBRAID | order_id + GCLID |
| Valor | Índice por etapa (§3) | Margen de contribución, no ingreso bruto |

Regla: **una sola conversión primaria por objetivo de negocio.** Varias primarias = el algoritmo optimiza
al promedio de cosas que no valen lo mismo.

## 2. Importación de etapas del CRM (inmobiliaria)

Flujo:

```
clic (gclid) → landing → formulario guarda gclid + email + teléfono → CRM
   → equipo comercial marca etapa → subida diaria/semanal a Google (etapa + valor + consent)
   → Smart Bidding aprende a comprar el perfil que llega a visita/reserva
```

Puntos críticos:

- **Si el CRM no guarda el GCLID contra cada lead, la importación offline no existe.** Es el fallo #1
  que bloquea todo el flujo de puja por valor. Solución: campo oculto en el formulario + persistencia
  del parámetro en cookie de primera parte.
- Camino recomendado hoy: **enhanced conversions for leads** (identificadores hasheados: email/teléfono)
  en lugar del offline conversion import clásico basado solo en GCLID — sobrevive mejor a la pérdida de cookies.
- **Ventana de 63 días**: conversiones subidas más de 63 días después del último clic no se importan.
  En ciclos inmobiliarios largos, esto obliga a definir la conversión primaria en una etapa que ocurra
  dentro de esa ventana (típicamente *lead calificado* o *visita agendada*, no *escritura*).
- Las subidas deben incluir el **estado de consentimiento** (`ad_user_data`, `ad_personalization`).
  Sin `ad_user_data = granted`, los datos hasheados se descartan del lado del servidor.
- Migración: las subidas se están moviendo a la **Data Manager API**; verifica en
  `CHANGELOG-plataforma.md` la fecha vigente antes de construir una integración nueva.

## 3. Valores por etapa (índice, no dinero real)

| Etapa CRM | Conversión en Google Ads | Valor índice |
|---|---|---|
| Formulario enviado | Lead | 1 |
| Contactado | Lead contactado | 5 |
| Calificado (presupuesto/financiamiento OK) | **Lead calificado** ← primaria | 25 |
| Visita agendada | Visita agendada | 60 |
| Visita realizada | Visita realizada | 120 |
| Reserva / promesa | Reserva | 600 |
| Escritura / venta | Venta | 3000 |

- Los valores deben reflejar la **probabilidad real de cierre** de cada etapa. Recalibrar cada trimestre
  con las tasas de conversión etapa→etapa observadas.
- Usar índice y no precio real evita exponer información comercial en la plataforma y facilita comparar
  proyectos de tickets distintos.
- Con esta escala se puede pasar a `Maximizar valor de conversión` + tROAS y el sistema deja de perseguir
  formularios baratos.

## 4. Calidad de datos — auditoría rápida (mensual)

- [ ] Conversión primaria única y sin duplicados (revisar que no haya dos tags del mismo evento).
- [ ] Diferencia Google Ads vs. CRM en volumen de leads <10%; si es mayor, hay pérdida de tracking.
- [ ] % de leads con GCLID capturado >90%.
- [ ] Enhanced conversions con estado "Grabando" y cobertura razonable.
- [ ] Consent Mode: verificar que el banner no bloquee el tag antes del consentimiento (y que el modelado funcione).
- [ ] Ventana de conversión coherente con el ciclo de compra (inmobiliaria: 60–90 días de clic;
      ecommerce: 30 días típico).
- [ ] Atribución: data-driven por defecto; si se compara histórico, indicar el modelo usado.
- [ ] Ecommerce: valor de conversión = margen (excluir impuestos, envío y devoluciones sistemáticas).

## 5. Señales de audiencia (1P)

- Customer Match con base de compradores/arrendatarios y con leads calificados históricos.
- Listas de exclusión: convertidos, clientes actuales, leads descalificados repetidos.
- Segmentos personalizados por intención (búsquedas de competencia, sitios de portales inmobiliarios).
- **Ojo en EE.UU./Canadá**: en vivienda, las audiencias curadas por el anunciante caen dentro del
  targeting restringido. Ver `politicas-y-riesgos.md` antes de configurar.
