# Propuesta Dale Coopeuch — Intothecom

Paquete de entregables para la propuesta de servicios de canales digitales a
Dale Coopeuch (dalecoopeuch.cl). Agosto 2026.

## Entregables

| # | Archivo | Formato | Destino |
|---|---------|---------|---------|
| 01 | `01_Propuesta_Economica_Dale_Coopeuch.pptx` | PPTX, 51 láminas | Drive → exportar PDF → cliente |
| 02 | `02_Plan_de_Medios_Dale_Coopeuch_Mes_Inicial.xlsx` | XLSX, 3 hojas | Drive → exportar PDF → cliente |
| 03 | `03_Investigacion_de_Mercado_Dale_Coopeuch.docx` | DOCX, 23 páginas | Documento de trabajo detallado |
| 04 | `04_Investigacion_de_Mercado_Resumen.pptx` | PPTX, 17 láminas | Resumen ejecutivo de la investigación |

## Servicios y valores

Sin descuentos por paquete. Valores mensuales.

| Servicio | Neto | IVA 19% | Total |
|---|---:|---:|---:|
| Paid Media | 35 UF | 6,65 UF | 41,65 UF |
| Community Management | 25 UF | 4,75 UF | 29,75 UF |
| Email Marketing | 25 UF | 4,75 UF | 29,75 UF |
| **Total servicios** | **85 UF** | **16,15 UF** | **101,15 UF** |

Datapify: USD 299 + IVA mensual, contratado directamente por el cliente con el
proveedor. Inversión en medios recomendada: $3.000.000 – $5.000.000 CLP mensuales.

## Estructura del plan de medios

Hoja 1 replica la estructura del plan de Diplas. Hoja 2 es el modelo de inversión
editable: al cambiar los supuestos naranjos se recalcula el costo por curse.
Hoja 3 lista los benchmarks con fuente y fecha.

## Pendientes de confirmación con el cliente

- Publicar CAE, plazos, montos y ejemplo representativo del costo total en la
  landing pública. Es requisito de Google Ads y hoy no está.
- Tasa de aprobación crediticia: único supuesto del modelo que no puede estimarse
  desde fuentes externas.
- Mapa de eventos de medición hasta el curse.
- Requisitos de verificación del anunciante en Google y Meta.

## Regeneración

`generadores/` contiene los scripts que producen los cuatro documentos. Requiere
`python-pptx`, `python-docx`, `openpyxl`, `pillow` y la tipografía Be Vietnam Pro.
Los valores comerciales están centralizados en `build_propuesta.py` y los
supuestos del modelo en `build_xlsx.py`.
