# Estado del proyecto — Propuesta Dale Coopeuch

Documento de traspaso. Última actualización: 27 de agosto de 2026.
Rama: `claude/dale-coopeuch-proposal-irivxw`.

Léelo completo antes de retomar. Contiene decisiones ya cerradas, correcciones
pendientes de aplicar y un bloqueante que debe resolverse antes de presentar.

---

## 1. El encargo

**Cliente potencial:** Dale Coopeuch (dalecoopeuch.cl), canal digital de Coopeuch.

**Objetivo comercial:** conversión y curse de créditos de consumo digitales captando
prospectos de mercado abierto. NO es awareness ni descargas de app.

**Servicios cotizados:** Paid Media, Community Management, Email Marketing y Datapify.
Sin SEO y sin Soporte Web.

**Etapa:** discovery. La propuesta económica es referencial y no vinculante; sirve para
que el cliente avance al NDA. No se redacta el NDA.

**Mecánica acordada:** las campañas llevan a WhatsApp, donde el agente IA de Datapify
levanta información, califica y deriva al prospecto calificado. La app deja de ser el eje
del embudo.

---

## 2. Decisiones cerradas — no volver a abrirlas

### Precios (confirmados por el equipo, sin descuento por paquete)

| Servicio | Neto | IVA 19% | Total |
|---|---:|---:|---:|
| Paid Media | 35 UF | 6,65 UF | 41,65 UF |
| Community Management | 25 UF | 4,75 UF | 29,75 UF |
| Email Marketing | 25 UF | 4,75 UF | 29,75 UF |
| **Total servicios** | **85 UF** | **16,15 UF** | **101,15 UF** |

- **Datapify: USD 299 + IVA mensual.** El cliente contrata directo con el proveedor.
  Se mantiene expresado en dólares, no se convierte a UF.
- Inversión en medios recomendada: **$3.000.000 – $5.000.000 CLP mensuales**, pagados
  directamente a cada plataforma, aparte del fee de agencia.
- Referencias del 26-ago-2026: UF $40.867,18 · dólar observado $911,43.

### Alcances

- **Community Management:** Instagram y TikTok. 2 publicaciones semanales en Instagram,
  2 historias semanales en Instagram, 2 publicaciones semanales en TikTok. Sin historias
  en TikTok y sin compensar con nada.
- **Sin grabación de contenidos.** No es un servicio que la agencia ofrezca en esta
  propuesta. Se trabaja con biblioteca de contenidos o material provisto por la marca.
  Debe quedar declarado en el alcance para evitar disputas posteriores.
- **Email Marketing:** 2 correos de campaña semanales más los flujos automatizados.
- **Datapify:** solo especificaciones, beneficios y tarifa. Sin comparativas contra
  agencias y sin el caso Imanix del brochure. El encuadre es complemento de las campañas.

### Condiciones comerciales

Las 13 aprobadas, en láminas separadas al final del deck para poder agregarlas o
quitarlas tras la revisión con el equipo. Permanencia mínima 6 meses. Aprobación de
piezas 48 horas hábiles. **Falta definir: días de pago de la factura.**

### Casos de éxito

Tres, uno por servicio ofrecido: Granja Magdalena (Paid Media), Inmobiliaria HCG
(Community Management) y Rebels Golf (Email Marketing). Imanix quedó fuera por ser caso
de SEO, servicio que no se está vendiendo. **Monteclaro no se menciona en ningún
documento**, se entregó solo como contexto interno.

### Diseño

Extraído del PDF de las propuestas base de Intothecom:

- Tipografía **Be Vietnam Pro** (está en Google Fonts, se ve bien en Google Slides).
- Naranjo primario `#E57000`; secundarios `#E69138` y `#F08C24`.
- Negros `#000000`, `#262626`, `#090909`. Grises `#7F7F7F`, `#595959`, `#EEEEEE`.
- Formato 10 × 5,625 pulgadas (16:9), nativo de Google Slides.
- Logos en PNG transparente en `generadores/assets/`.
- Navegación superior con subrayado naranjo, footer en todas las láminas, portada negra,
  divisores con botón "Continuar →".

---

## 3. BLOQUEANTE — resolver antes de presentar

**Puede que Google Search esté cerrado para esta categoría en Chile.**

Un integrante del equipo observó que al buscar "crédito de consumo" en Google no aparecen
resultados de pago. Coincide con que ningún sitio revisado —Dale, Coopeuch ni los bancos—
publica las divulgaciones que Google exige.

**Lo verificado con documentación oficial:**

- La política de préstamos personales aplica en Chile: *"independientemente de la
  ubicación de segmentación"*.
- Exige mostrar de forma destacada en la landing o app: plazo mínimo y máximo de pago,
  CAE máxima separada del ejemplo, y ejemplo representativo del costo total incluidas
  comisiones.
- **Las divulgaciones no pueden estar tras un clic ni un hover**, ni en otra pestaña o
  vínculo. Esto descarta acordeones y modales, y debilita mucho la opción de dejarlas
  dentro de la app tras el login.
- Divulgaciones adicionales para todo producto financiero: dirección física de la empresa,
  comisiones asociadas y vínculos a acreditación externa.
- Solo se permiten préstamos con pago íntegro en 61 días o más.
- **El tope de TAE 36% es exclusivo de EE.UU.** Fuera de ese mercado los anuncios son
  aptos. Esto es determinante porque la CAE chilena suele superar ese umbral. El estado
  aparecerá como "Apto (limitado)", que es etiqueta informativa y no bloqueo.
- **Chile no está en la lista de verificación de servicios financieros.** Son 42 países
  (verificado en la versión en inglés), incluidos Brasil y Turquía. Chile no.
- La política excluye las líneas de crédito rotativo. Por eso Tenpo y MACH, que venden
  cuenta, prepago y tarjeta de crédito, no están sujetos a ella. Dale sí, si el Crédito
  Digital es un crédito en cuotas — **confirmar con el cliente**.

**Verificado también:** la Ley 20.555 (SERNAC Financiero) ya obliga a informar la CAE en
publicidad de créditos que mencione cuota o tasa de referencia. Google es más exigente:
lo pide en la landing con independencia de lo que diga el anuncio.

**Lo que NO se pudo verificar desde el entorno remoto:** si los competidores cumplen, y si
efectivamente hay o no anuncios activos. Fallaron tres vías: lectura de HTML crudo (falsos
negativos en sitios JavaScript), navegador headless (bloqueado por el proxy) y la API del
Centro de Transparencia de Anuncios (formato de consulta no resuelto; con Nike como
control también devuelve vacío, así que los resultados no valen).

### Tests pendientes, en orden de contundencia

1. **Anuncio de prueba en la cuenta de Intothecom.** Presupuesto mínimo, anuncio apuntando
   a `dalecoopeuch.cl/creditodigital`, enviar a revisión SIN activar. Google responde en
   24–48 h con aprobación o rechazo y el motivo exacto. Costo cero. Es el definitivo.
2. **Centro de Transparencia de Anuncios** (`adstransparency.google.com`), filtro Chile,
   buscar Coopeuch, BancoEstado, Santander, Forum, Falabella. Diez minutos con navegador.
   Si alguno corre anuncios, abrir su URL de destino y ver cómo resolvió la divulgación.
3. **Keyword Planner** de la cuenta propia: si la competencia es nula, corrobora.
4. **SERP limpio**: incógnito, sin bloqueador, ubicación Chile, varios términos y horarios.

### Consecuencia para el plan de medios

- **Si Search funciona:** el plan queda como está.
- **Si Search está cerrado:** reestructurar antes de presentar. Tres de las seis campañas
  son Search y representan el 40% de la inversión. Meta CTWA pasaría a canal principal, la
  inversión se redistribuye hacia Meta y Demand Gen, y publicar las condiciones en la
  landing deja de ser requisito técnico para ser la condición que habilita un canal
  completo. Bien planteado es un argumento de venta fuerte.
- **Meta no se ve afectado en ningún escenario.** La política es de Google.

---

## 4. Correcciones pendientes de aplicar a los documentos

Están redactadas y aprobadas conceptualmente, pero **todavía no se aplicaron a los
archivos**. El equipo pidió recibir el texto para pegarlo manualmente.

### 4.1 Remanente — cuatro ubicaciones

La redacción original decía "devolución anual de utilidades a los Socios" y afirmaba que
Tenpo, MACH y Mercado Pago no tienen equivalente. Ambas cosas eran imprecisas: una
cooperativa reparte remanente, no utilidades, y la comparación competitiva era inferencia
sin fuente.

Definición oficial (coopeuch.cl/personas/remanente.html): *"El Remanente es el resultado
anual de nuestra cooperativa menos el reajuste de las cuotas de participación. Su
distribución se aprueba en la Junta de Delegados... las personas que lo reciben son socias
y socios vigentes al 31 de diciembre"*.

El sitio de Dale sí lo menciona, en el cuerpo de la landing del crédito: *"Cada vez que
pagas tu crédito, tu remanente como Socio crece, y eso permite que más personas puedan
acceder a financiamiento justo y solidario"*.

Ubicaciones a corregir: **DOCX págs. 6, 17 y 22** y **Resumen PPTX lámina 5**.

### 4.2 Sección 5.1 del DOCX (pág. 10)

Reemplazar los cuatro bullets por siete, incorporando: alcance y exclusión de líneas
rotativas, la regla de visibilidad sin interacción, las divulgaciones adicionales de todo
producto financiero, y que el tope de TAE 36% no aplica en Chile.

### 4.3 Nota de verificación del capítulo 5.2

Reemplazar el pendiente de verificación por el argumento de que Tenpo y MACH no están
sujetos a la política, y que Google evalúa la landing del anuncio y no el sitio
corporativo.

---

## 5. Entregables

| # | Archivo | Estado |
|---|---|---|
| 01 | `01_Propuesta_Economica_Dale_Coopeuch.pptx` | 51 láminas, verificado en PDF |
| 02 | `02_Plan_de_Medios_Dale_Coopeuch_Mes_Inicial.xlsx` | 3 hojas, una página horizontal |
| 03 | `03_Investigacion_de_Mercado_Dale_Coopeuch.docx` | 23 páginas |
| 04 | `04_Investigacion_de_Mercado_Resumen.pptx` | 17 láminas |

`generadores/` contiene los scripts que producen los cuatro. Requiere `python-pptx`,
`python-docx`, `openpyxl`, `pymupdf`, `pillow` y la fuente Be Vietnam Pro. Los valores
comerciales están en `build_propuesta.py`; los supuestos del modelo en `build_xlsx.py`.

Para verificar visualmente: convertir a PDF con LibreOffice y renderizar las páginas.
Requiere `libreoffice-impress`, `libreoffice-calc` y `libreoffice-writer` instalados.

---

## 6. Modelo de inversión

Construido de abajo hacia arriba, no copiando un promedio de mercado. **No existe una
cifra pública confiable de inversión mensual por anunciante financiero en Chile** — AAM,
Admetricks e IAB Chile publican agregados, no gasto por anunciante.

CPC triangulado cruzando dos fuentes independientes: benchmark de EE.UU. convertido
($2.807–$3.154 CLP) contra reportes locales de financiamiento ($2.000–$3.000 CLP).
Banda de trabajo: **$2.400–$3.200 CLP**. Chile está en torno al 60–80% del CPC
estadounidense, no en la fracción mucho menor que suele asumirse.

Escenario de $3.500.000 CLP mensuales: ~2.970 clics, ~678 conversaciones, ~237 prospectos
calificados a ~$14.800, ~47 cursos a ~$74.500.

**La tasa de aprobación a curse (20% en el modelo) es un marcador de posición.** Es el
único supuesto que no puede estimarse desde fuentes externas: depende de la política de
riesgo de Coopeuch y debe aportarlo el cliente.

---

## 7. Pendientes con el cliente

1. Publicar CAE, plazos, montos y ejemplo representativo del costo total en la landing
   pública, visibles sin interacción.
2. Confirmar la tasa de aprobación crediticia.
3. Confirmar si el Crédito Digital es un crédito en cuotas o una línea rotativa.
4. Definir el mapa de eventos de medición hasta el curse.
5. Verificar requisitos de verificación del anunciante en Google y Meta al implementar.

## 8. Pendientes internos

1. Correr los tests de viabilidad de Search (sección 3).
2. Definir días de pago de la factura para las condiciones comerciales.
3. Aplicar las correcciones de la sección 4.
4. Relevamiento de anuncios de referencia en el Centro de Transparencia y la Biblioteca de
   Anuncios de Meta. No se incluyeron capturas de piezas de terceros por no poder
   verificarlas; queda como primera actividad del onboarding.

---

## 9. Criterios de trabajo acordados

- **Tarifas completas, sin descuentos por paquete.** Ojo con los precios.
- **No inventar información sensible.** Todo dato con fuente y fecha. Lo que no se puede
  respaldar se declara como pendiente, no se rellena.
- **Mantener el diseño de las propuestas base.** No rediseñar, no perder tiempo en
  estética nueva.
- Los benchmarks internacionales se usan como referencia de la relación entre métricas,
  nunca como valor absoluto trasladable a Chile.
