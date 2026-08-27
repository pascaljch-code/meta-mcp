# Estado del proyecto — Propuesta Dale Coopeuch

Documento de traspaso. Última actualización: 27 de agosto de 2026.
Rama: `claude/dale-coopeuch-proposal-irivxw`.

Léelo completo antes de retomar. Contiene las decisiones ya cerradas y siete correcciones
redactadas que **todavía no se han aplicado a los archivos**. No hay bloqueantes abiertos:
la viabilidad de Google Search quedó resuelta y está documentada en la sección 3.

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

## 3. Viabilidad de Google Search — RESUELTO

**Search está abierto para esta categoría en Chile.** Hubo una hipótesis intermedia de que
el requisito de divulgación podía haber cerrado la categoría, y era incorrecta. Se descartó
con evidencia directa: capturas de resultados patrocinados reales para "crédito" y "crédito
de consumo" mostrando anuncios activos de Banco BICE, Itaú, Santander, Bci, Destacame,
ComparaOnline y Almagro. **El plan de medios se mantiene con sus tres campañas de Search.**

### Lo verificado sobre la política de Google

- Aplica en Chile: *"independientemente de la ubicación de segmentación"*.
- Exige mostrar de forma destacada en la landing o app: plazo mínimo y máximo de pago,
  CAE máxima separada del ejemplo, y ejemplo representativo del costo total incluidas
  comisiones.
- **Las divulgaciones no pueden estar tras un clic ni un hover**, ni en otra pestaña o
  vínculo. Descarta acordeones y modales, y debilita la opción de dejarlas dentro de la app
  tras el login.
- Divulgaciones adicionales para todo producto financiero: dirección física de la empresa,
  comisiones asociadas y vínculos a acreditación externa.
- Solo préstamos con pago íntegro en 61 días o más.
- **El tope de TAE 36% es exclusivo de EE.UU.** Fuera de ese mercado los anuncios son
  aptos. Determinante porque la CAE chilena suele superar ese umbral. El estado aparece
  como "Apto (limitado)", etiqueta informativa y no bloqueo.
- **Chile no está en la lista de verificación de servicios financieros**: 42 países
  (verificado en la versión en inglés), incluidos Brasil y Turquía. Chile no.
- La política excluye las líneas de crédito rotativo. Por eso Tenpo y MACH, que venden
  cuenta, prepago y tarjeta de crédito, no están sujetos. Dale sí, si el Crédito Digital es
  un crédito en cuotas — **confirmar con el cliente**.
- La Ley 20.555 (SERNAC Financiero) ya obliga a informar la CAE en publicidad de créditos
  que mencione cuota o tasa de referencia. Google es más exigente: lo pide en la landing con
  independencia de lo que diga el anuncio.

### Cómo lo resuelve el mercado — landings de anuncios reales

| Anunciante | Producto | ¿Publica condiciones? | Verificación |
|---|---|---|---|
| Almagro / MetLife | Hipotecario | **Sí, completo**: tasa fija UF + 3,43%, CAE 4,08%, ejemplo con monto UF 3.200, plazo 30 años y dividendo $608.362 | Página leída íntegra |
| Destacame | Crédito de consumo | **No**: solo montos referenciales; declara que monto, plazo, tasa y condiciones se informan antes de contratar | Página leída íntegra |
| ComparaOnline | Comparador | Parcial: explica la CAE y despliega valores por institución vía simulador | Parcial |
| Santander · BICE · Itaú | Crédito de consumo | No verificable | WAF / contenido JavaScript |

Tres modelos identificados:

1. **Ejemplo representativo estático** (Almagro). El más limpio. Bloque de contenido visible
   sin interacción. Notable: los hipotecarios están excluidos de la política de Google y aun
   así cumple, porque la Ley 20.555 se lo exige al mencionar tasa.
2. **Simulador embebido** (ComparaOnline y probablemente los bancos). Cumple, pero requiere
   desarrollo.
3. **Reencuadre del producto** (Destacame). Es el competidor más parecido a Dale por perfil.
   Corre anuncios sin publicar CAE, tasa, plazos ni ejemplo. Su producto son "montos
   escalonados que crecen contigo" accesibles mediante suscripción, lo que puede situarlo
   fuera de la definición de préstamo no recurrente. No se puede determinar desde fuera si
   opera bajo esa exclusión, si lo anunciado es la suscripción, o si no ha sido fiscalizado.

### Recomendación adoptada

**Modelo 1, ejemplo representativo estático.** Es el más económico de implementar, satisface
Google y la Ley 20.555 al mismo tiempo, y no depende de cómo esté estructurado el producto.
Las dos primeras salidas del modelo 3 dependen de definiciones que la marca no controla
frente a un revisor externo, y la tercera consiste en confiar en no ser fiscalizado, lo que
no es alternativa para una entidad supervisada por la CMF.

Especificación del bloque a publicar en `dalecoopeuch.cl/creditodigital`:

```
Ejemplo representativo del Crédito Digital Dale
Monto: $[X] · Plazo: [N] cuotas · Tasa de interés: [X]% mensual
CAE: [X]% · Valor cuota: $[X] · Costo total del crédito: $[X]
Incluye [comisiones y seguros aplicables]
Plazo mínimo: [N] cuotas · Plazo máximo: [N] cuotas · CAE máxima: [X]%
Crédito sujeto a evaluación y aprobación crediticia
[Razón social y dirección física de la entidad que otorga el crédito]
```

Cuatro condiciones: la CAE máxima va separada del ejemplo; nada detrás de acordeón, pestaña,
modal o "ver más"; incluir dirección física de la entidad otorgante; el bloque va en la
landing pública, no dentro de la app tras el login.

### Nota sobre el copy del anuncio

Mencionar cuota o tasa en el aviso activa la obligación de CAE bajo la Ley 20.555. Google
exige el ejemplo en la landing sin importar qué diga el aviso. Configuración más segura: el
anuncio evita tasas y cuotas, y la landing carga el ejemplo representativo. Se cumple por
ambos lados y queda libertad creativa en el copy.


## 4. Correcciones pendientes de aplicar a los documentos

Están redactadas y entregadas al equipo para pegado manual. **Ninguna se ha aplicado
todavía a los archivos.** Si retomas el trabajo, verifica primero cuáles ya fueron pegadas
antes de regenerar nada desde los scripts.

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

Ubicaciones: **DOCX págs. 6, 17 y 22** y **Resumen PPTX lámina 5**.

### 4.2 DOCX sección 5.1 — pág. 8

Reemplazar los cuatro bullets por siete: alcance y exclusión de líneas rotativas, las tres
divulgaciones del crédito, la regla de visibilidad sin interacción, las divulgaciones
adicionales de todo producto financiero, la regla de 61 días, que el tope de TAE 36% no
aplica en Chile, y el sistema de faltas. Más nota de fuente con fecha de verificación.

### 4.3 DOCX sección 5.2 — págs. 8 y 9 · la reescritura más importante

Retitular a **"5.2 Cómo resuelve esto el mercado chileno"** y reemplazar el párrafo
introductorio, la tabla de tres filas y el recuadro "Nota de verificación" por: el marco de
la Ley 20.555, la diferencia entre el gatillo chileno y el de Google, la tabla de landings
reales relevadas, el análisis de los tres modelos y el recuadro de recomendación. El
contenido está en la sección 3 de este documento.

### 4.4 DOCX — nueva sección 5.4

Insertar después de 5.3 la especificación del bloque a publicar, con las cuatro condiciones
de implementación. Contenido en la sección 3 de este documento.

### 4.5 DOCX sección 10.1 — pág. 18

Reemplazar el recuadro "Alcance declarado" por uno que remita al relevamiento real del
capítulo 5.2 y deje el barrido sistemático de la Biblioteca de Anuncios de Meta y el Centro
de Transparencia de Google como actividad de onboarding.

### 4.6 DOCX sección 12.1 — pág. 22

Reemplazar el primer bullet por uno que apunte a las secciones 5.4 y 5.2 y que enfatice que
es un bloque de contenido, no un desarrollo: se resuelve en días.

### 4.7 Resumen PPTX lámina 8

Reemplazar subtítulo y los cuatro bullets por cinco, incorporando la regla de visibilidad
sin interacción, cómo lo resuelve el mercado y que la exigencia se apoya en la Ley 20.555.

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

1. **Publicar el bloque de ejemplo representativo** en la landing pública, visible sin
   interacción. Especificación exacta en la sección 3. Es lo único que hoy bloquea las
   campañas de búsqueda, y es un bloque de contenido, no un desarrollo.
2. Confirmar la tasa de aprobación crediticia.
3. Confirmar si el Crédito Digital es un crédito en cuotas o una línea rotativa.
4. Definir el mapa de eventos de medición hasta el curse.
5. Verificar requisitos de verificación del anunciante en Google y Meta al implementar.

## 8. Pendientes internos

1. **Aplicar las siete correcciones de la sección 4.** Es lo más urgente: los documentos
   entregados todavía contienen la redacción anterior.
2. Definir días de pago de la factura para las condiciones comerciales.
3. Relevamiento sistemático de anuncios de la competencia en el Centro de Transparencia de
   Google Ads y la Biblioteca de Anuncios de Meta. Ya se relevaron landings reales (sección
   3), falta el barrido de piezas y su antigüedad. Queda como actividad de onboarding.
4. Verificar de nuevo las políticas de plataforma antes del lanzamiento. La verificación
   vigente es del 26 y 27 de agosto de 2026.

---

## 9. Criterios de trabajo acordados

- **Tarifas completas, sin descuentos por paquete.** Ojo con los precios.
- **No inventar información sensible.** Todo dato con fuente y fecha. Lo que no se puede
  respaldar se declara como pendiente, no se rellena.
- **Mantener el diseño de las propuestas base.** No rediseñar, no perder tiempo en
  estética nueva.
- Los benchmarks internacionales se usan como referencia de la relación entre métricas,
  nunca como valor absoluto trasladable a Chile.
