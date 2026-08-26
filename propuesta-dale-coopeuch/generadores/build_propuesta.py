# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/tmp/claude-0/-home-user-meta-mcp/3417b367-2cff-5bc9-8662-cddb20c827cd/scratchpad")
from deck_lib import *
from slides import *
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

OUT = "/home/user/meta-mcp/propuesta-dale-coopeuch/01_Propuesta_Economica_Dale_Coopeuch.pptx"
prs = new_deck()
P = PHOTO

# ══════════════════════════ 0. APERTURA ═══════════════════════════════════════
s_cover(prs, "Dale Coopeuch",
        "Paid Media · Community Management · Email Marketing · Datapify")

# ¿Quiénes somos?
sl = blank(prs); rect(sl, 0, 0, W, H, fill=WHITE)
picture_cover(sl, f"{P}/laptop_neon.jpeg", Inches(4.92), 0, Inches(5.08), Inches(2.78))
rect(sl, Inches(4.92), Inches(2.78), Inches(5.08), Inches(2.845), fill=ORANGE)
accent_arrow(sl, Inches(0.46), Inches(1.10), h=Inches(0.72))
title2(sl, Inches(0.82), Inches(1.05), "¿Quiénes", "Somos?", size=26, w=Inches(3.7))
txt(sl, Inches(0.82), Inches(2.06), Inches(3.6), Inches(0.3),
    "Un equipo de alto rendimiento", size=10, bold=True, color=INK)
txt(sl, Inches(0.82), Inches(2.42), Inches(3.65), Inches(2.3),
    "Somos una agencia de marketing digital especializada en impulsar el crecimiento y la "
    "visibilidad de tu negocio a través de estrategias innovadoras y personalizadas.\n\n"
    "Nos enfocamos en comprender a fondo las necesidades de cada negocio para ofrecer "
    "soluciones digitales efectivas que optimicen su presencia en el mercado.\n\n"
    "Con un firme compromiso con la excelencia y la calidad, trabajamos para generar "
    "resultados medibles y sostenibles.", size=8.6, color=GRAY, spacing=1.35)
txt(sl, Inches(5.42), Inches(3.20), Inches(4.1), Inches(0.6),
    "Complicidad con el cliente", size=16, color=WHITE, bold=False, spacing=1.1)
txt(sl, Inches(5.42), Inches(3.92), Inches(4.05), Inches(1.0),
    "Nos involucramos en tu negocio como si fuera el nuestro. Te entregamos la confianza y "
    "dedicación que necesitas para potenciar tu marca hacia nuevos niveles.",
    size=8.6, color=WHITE, spacing=1.3)
footer(sl)

# Filosofía
sl = blank(prs); rect(sl, 0, 0, W, H, fill=WHITE)
title2(sl, Inches(0.62), Inches(0.75), "Nuestra", "Filosofía de Trabajo", size=24,
       w=Inches(4.6))
vals = [("VALOR", "Nos enfocamos en ofrecer un servicio de alta calidad, diseñado para aportar "
                  "un impacto real y positivo en tu organización. Nuestro compromiso es brindar "
                  "soluciones efectivas y estratégicas que impulsen el crecimiento."),
        ("COMUNIDAD", "Creemos en la importancia del trabajo colaborativo y en la construcción "
                      "de relaciones duraderas con nuestros clientes. Nos involucramos en cada "
                      "proyecto como un aliado estratégico."),
        ("RESULTADOS", "Cada estrategia que implementamos está orientada a resultados concretos "
                       "y medibles, utilizando métricas y análisis de datos para optimizar el "
                       "rendimiento y maximizar el retorno.")]
x = Inches(0.42)
for i, (h, d) in enumerate(vals):
    card(sl, x, Inches(2.05), Inches(2.98), Inches(2.62),
         fill=INK if i == 1 else RGBColor(0xFA, 0xFA, 0xFA), radius=0.05)
    txt(sl, x + Inches(0.28), Inches(2.34), Inches(2.5), Inches(0.3), h, size=13,
        bold=True, color=ORANGE)
    txt(sl, x + Inches(0.28), Inches(2.78), Inches(2.45), Inches(1.6), d, size=8.4,
        color=LINE if i == 1 else GRAY, spacing=1.35)
    x += Inches(3.12)
footer(sl)

# Ecosistema
s_split(prs, None, "Ecosistema", "Digital Integral",
        body="En Intothecom potenciamos un ecosistema digital integral que conecta "
             "estratégicamente cada canal para maximizar el rendimiento.\n\n"
             "Desde Paid Media, Redes Sociales, Email Marketing y plataformas "
             "conversacionales, integramos datos clave provenientes de las diferentes "
             "fuentes, permitiendo trabajar, analizar y optimizar las estrategias de "
             "manera eficiente.\n\n"
             "Nuestro enfoque permite visualizar el impacto de cada canal en el "
             "crecimiento del negocio, ofreciendo insights accionables y mediciones "
             "precisas para una toma de decisiones basada en datos.",
        photo=f"{P}/desk_wide.jpeg", photo_side="left", accent=False)

# ══════════════════════════ 1. EL DESAFÍO ═════════════════════════════════════
s_divider(prs, "EL DESAFÍO",
          "Entendemos que el objetivo no es notoriedad ni descargas: es la conversión y el "
          "curse de créditos de consumo. Todo lo que proponemos está construido sobre esa "
          "premisa.", f"{P}/caso_laptop.jpeg", active="Paid Media")

s_split(prs, "Paid Media", "El objetivo:", "curse, no awareness",
        body="El requerimiento es claro: llegar a prospectos de mercado abierto y convertirlos "
             "en créditos de consumo cursados. El awareness y el uso de la app son "
             "consecuencia, no meta.",
        items=[("Tráfico no es el problema. ", "El desafío está en la conversión: mover al "
                "prospecto desde el interés hasta la contratación efectiva."),
               ("El curse es el KPI. ", "Optimizar a \"lead\" genera volumen que el área "
                "comercial no necesariamente cierra. Medimos hasta el final del embudo."),
               ("Mercado abierto exige calificación. ", "Un prospecto frío requiere ser "
                "levantado, calificado y derivado antes de llegar al área comercial.")],
        photo=f"{P}/desk_vertical.jpeg")

s_numbered(prs, "Paid Media", "El embudo", "que vamos a atacar",
           intro="Cada etapa es un punto de fuga medible. La estrategia consiste en reducir "
                 "la fricción en cada una y recuperar al usuario que no avanza.",
           photos=[f"{P}/office_vertical.jpeg", f"{P}/desk_wide.jpeg"],
           entries=[("01.", "Captación",
                     "Campañas en Google y Meta que capturan demanda existente de crédito de "
                     "consumo y generan demanda en el nicho desatendido de trabajadores "
                     "independientes."),
                    ("02.", "Conversación y calificación",
                     "El anuncio deriva a WhatsApp, donde el agente de IA levanta información, "
                     "resuelve dudas y califica al prospecto según los criterios que defina "
                     "la marca."),
                    ("03.", "Derivación y curse",
                     "Solo el prospecto calificado se deriva al proceso de contratación. "
                     "Email y remarketing recuperan a quienes no completaron el proceso.")])

s_split(prs, "Paid Media", "La estrategia:", "conversación calificada",
        body="En vez de enviar tráfico frío a un formulario, lo llevamos a una conversación "
             "asistida por IA en WhatsApp. Esto cambia la economía del embudo.",
        items=[("Menor fricción de entrada. ", "Iniciar una conversación exige menos "
                "compromiso que completar una solicitud."),
               ("Calificación antes de derivar. ", "El área comercial recibe prospectos "
                "filtrados, no volumen bruto."),
               ("Resolución de objeciones en tiempo real. ", "En crédito digital la principal "
                "barrera es la desconfianza y las dudas sobre el proceso."),
               ("Disponibilidad permanente. ", "La intención de solicitar un crédito no "
                "respeta el horario de oficina.")],
        photo=f"{P}/caso_laptop.jpeg")




# ══════════════════════════ 2. PAID MEDIA ═════════════════════════════════════
s_divider(prs, "PAID MEDIA\n(ADS)",
          "Resultados medibles, inversión optimizada y conversiones al máximo. Descubre cómo "
          "nuestras estrategias de Paid Media generan impacto y rentabilidad en cada campaña.",
          f"{P}/div_casos.jpeg", active="Paid Media")

s_split(prs, "Paid Media", "¿En qué consiste", "Paid Media?",
        body="Paid Media se basa en anuncios pagados para aparecer en las primeras posiciones "
             "de los resultados de búsqueda y en las distintas plataformas.",
        items=[("Centrado en aumentar el tráfico calificado: ", "el tráfico pagado vía Google "
                "y Meta se centra en llevar leads calificados al canal de conversión."),
               ("Aumenta la cantidad y la calidad: ", "pagando por anuncios logramos llevar al "
                "público que necesitamos hacia el punto de contratación."),
               ("Corto y largo plazo: ", "si bien tiene resultados esperables en el corto "
                "plazo, en el largo plazo es muy beneficioso porque las estrategias se van "
                "optimizando constantemente.")],
        photo=f"{P}/office_wide.jpeg")

s_grid(prs, "Paid Media", "Importancia de la Publicidad Digital",
       [("Alcance", "Llegar a una audiencia amplia y diversa, con control preciso sobre la "
                    "cobertura geográfica."),
        ("Segmentación", "Capacidad para dirigir la inversión hacia perfiles específicos y "
                         "audiencias de alto valor."),
        ("Rentabilidad", "La publicidad digital suele ser más rentable, ofreciendo un mejor "
                         "retorno sobre la inversión."),
        ("Análisis y medición", "Capacidad de medir y analizar los resultados de las campañas "
                                "en tiempo real y corregir sobre la marcha.")],
       cols=4, sub="Paid Media Ads")

s_numbered(prs, "Paid Media", "¿Cómo lo", "trabajamos?",
           intro="Metodología utilizada para la creación, medición y optimización de campañas.",
           photos=[f"{P}/desk_vertical.jpeg", f"{P}/laptop_neon.jpeg"],
           entries=[("01.", "Meta Objetivo",
                     "Definimos objetivos claros y medibles. Según estos objetivos se elige la "
                     "combinación ideal de medios y tipos de campañas para maximizar resultados."),
                    ("02.", "Investigación de KeyWords",
                     "Definidos los KPI, se investigan palabras clave relevantes priorizando "
                     "alto valor e intención de contratación, además de keywords negativas."),
                    ("03.", "Segmentación de Audiencias",
                     "La segmentación optimiza campañas y reduce gasto innecesario, alineada a "
                     "las recomendaciones vigentes de cada plataforma.")])

s_numbered(prs, "Paid Media", "¿Cómo lo", "trabajamos?",
           intro="La ejecución y el control son tan importantes como la planificación inicial.",
           photos=[f"{P}/office_vertical.jpeg", f"{P}/caso_laptop.jpeg"],
           entries=[("04.", "Creación de Ads",
                     "Se desarrollan y analizan títulos, descripciones, piezas gráficas, "
                     "enlaces, CTA y keywords, con foco en la claridad del mensaje."),
                    ("05.", "Presupuesto y Programación",
                     "Presupuesto diario y estrategia de puja acordes a los objetivos, "
                     "programando los anuncios en los momentos clave para el público."),
                    ("06.", "Seguimiento de Campañas",
                     "Medición continua del rendimiento con seguimiento de conversiones "
                     "mediante Google Ads, GA4 y Looker Studio.")])

s_split(prs, "Paid Media", "Ajuste y análisis", "continuo",
        body="El mercado publicitario es dinámico: lo que funciona un mes puede dejar de "
             "hacerlo al siguiente. Por eso el trabajo no termina con el lanzamiento.",
        items=[("07. Ajustes de campañas. ", "Pruebas A/B, optimización de estrategias de puja "
                "y presupuesto, y refinamiento de keywords y audiencias según los datos."),
               ("08. Análisis de anuncios y competencia. ", "Monitoreo de keywords, mensajes y "
                "posiciones de la competencia para identificar oportunidades y amenazas.")],
        photo=f"{P}/desk_wide.jpeg")

# Estructura de campañas propuesta (específico del cliente)
sl = blank(prs); rect(sl, 0, 0, W, H, fill=WHITE); navbar(sl, active="Paid Media")
title1(sl, Inches(0.6), Inches(0.82), "Estructura de Campañas Propuesta", size=22,
       w=Inches(8.8), align=PP_ALIGN.CENTER)
txt(sl, Inches(1.0), Inches(1.32), Inches(8.0), Inches(0.3),
    "Seis campañas base. La inversión detallada se presenta en el Plan de Medios adjunto.",
    size=9.5, color=GRAY, align=PP_ALIGN.CENTER)
camp = [("Google Ads", "Search | Marca",
         "Protege el término propio y captura la demanda ya generada."),
        ("Google Ads", "Search | Genérica",
         "Demanda de alta intención sobre crédito de consumo digital."),
        ("Google Ads", "Search | Inclusión",
         "Nicho de independientes y personas sin liquidación de sueldo."),
        ("Meta Ads", "CTWA | Prospección",
         "Click to WhatsApp con segmentación amplia para mercado abierto."),
        ("Meta Ads", "CTWA | Inclusión",
         "Testea el diferenciador de evaluación con múltiples fuentes de ingreso."),
        ("Meta Ads", "Retargeting",
         "Recupera a quien interactuó o inició conversación sin completar.")]
x0, y0 = Inches(0.42), Inches(1.85)
cw, chh = Inches(3.06), Inches(1.52)
for i, (canal, tipo, desc) in enumerate(camp):
    r, c = divmod(i, 3)
    x = x0 + (cw + Inches(0.11)) * c
    y = y0 + (chh + Inches(0.16)) * r
    card(sl, x, y, cw, chh, fill=RGBColor(0xFA, 0xFA, 0xFA), radius=0.06)
    pill(sl, x + Inches(0.18), y + Inches(0.17), Inches(1.05), Inches(0.24), canal,
         size=7.5)
    txt(sl, x + Inches(0.18), y + Inches(0.55), cw - Inches(0.36), Inches(0.25), tipo,
        size=11, bold=True, color=INK)
    txt(sl, x + Inches(0.18), y + Inches(0.86), cw - Inches(0.36), Inches(0.6), desc,
        size=8.4, color=GRAY, spacing=1.25)
footer(sl)

# Consideraciones regulatorias
s_text(prs, "Paid Media", "Consideraciones regulatorias del canal",
       sub="La publicidad de crédito de consumo opera bajo reglas específicas de cada "
           "plataforma. Levantamos estos puntos antes de invertir, no después.",
       items=[("Divulgación obligatoria en la landing. ", "Google exige mostrar de forma "
               "destacada el plazo mínimo y máximo de pago, la CAE máxima y un ejemplo "
               "representativo del costo total incluidas comisiones. Es requisito previo al "
               "lanzamiento."),
              ("Regla de los 61 días. ", "Solo se permiten préstamos personales que requieren "
               "el pago íntegro en 61 días o más."),
              ("Segmentación 18+. ", "Los anuncios de crédito deben dirigirse exclusivamente a "
               "mayores de 18 años."),
              ("Verificación del anunciante. ", "Meta puede requerir verificación de identidad "
               "y acreditación ante el organismo regulador correspondiente."),
              ("Buena noticia sobre segmentación. ", "Las restricciones de categoría especial "
               "de Meta aplican a Estados Unidos, Canadá y parte de Europa. En Chile "
               "conservamos audiencias personalizadas, lookalikes y segmentación detallada.")],
       size=9.3)

# ══════════════════════════ 3. COMMUNITY MANAGEMENT ═══════════════════════════
s_divider(prs, "COMMUNITY\nMANAGEMENT",
          "Construimos comunidades, fortalecemos marcas y generamos conversaciones auténticas. "
          "Descubre cómo nuestra estrategia crea conexiones que impactan.",
          f"{P}/div_cm.jpeg", active="Community M.")

s_split(prs, "Community M.", "¿Qué es el", "Community Management?",
        body="Es la gestión, construcción y moderación de comunidades en línea en torno a una "
             "marca, principalmente en redes sociales y otros canales digitales.\n\n"
             "Lo realiza un Community Manager, cuyo rol es actuar como la voz de la marca en "
             "el espacio digital, estableciendo una relación directa y personal con la "
             "audiencia y los clientes.",
        items=[("En un servicio financiero el rol es distinto: ", "la comunidad no se "
                "construye sobre entretenimiento sino sobre confianza, claridad del proceso y "
                "resolución de dudas.")],
        photo=f"{P}/office_vertical.jpeg")

s_grid(prs, "Community M.", "Funciones Claves del Community Management",
       [("Gestión de RRSS", "Creación, programación y publicación de contenido relevante."),
        ("Estrategia contenido", "Alinear publicaciones con los valores, estilo y objetivos de "
                                 "la marca."),
        ("Interacción comunidad", "Responder comentarios y mensajes, y gestionar situaciones "
                                  "de reputación."),
        ("Análisis y reporte", "Medir el rendimiento, optimizar estrategias y ajustar "
                               "tácticas."),
        ("Gestión de crisis", "Estrategias y acciones para manejar situaciones que puedan "
                              "afectar la reputación."),
        ("Monitoreo competencia", "Identificar tendencias y oportunidades utilizadas en el "
                                  "mercado.")],
       cols=3)

# Rol por plataforma (solo IG + TikTok)
sl = blank(prs); rect(sl, 0, 0, W, H, fill=WHITE); navbar(sl, active="Community M.")
title1(sl, Inches(0.6), Inches(0.85), "Rol por Plataforma", size=23, w=Inches(8.8),
       align=PP_ALIGN.CENTER)
plats = [("INSTAGRAM", "Rol interactivo",
          "El aspecto visual es clave para captar la atención, combinado con contenido que "
          "fomente la participación y construcción de comunidad. Se aprovechan historias "
          "interactivas, enlaces, videos cortos y transmisiones en vivo para mejorar la "
          "conexión con la audiencia."),
         ("TIKTOK", "Rol de visibilidad",
          "Ideal para contenido en tendencia, auténtico y creativo, potenciando el "
          "reconocimiento de marca. Su algoritmo muestra videos según las preferencias del "
          "usuario, facilitando la exploración de nuevos segmentos de mercado.")]
x = Inches(0.62)
for i, (name, rol, desc) in enumerate(plats):
    card(sl, x, Inches(1.62), Inches(4.2), Inches(3.05),
         fill=INK if i == 0 else RGBColor(0xFA, 0xFA, 0xFA), radius=0.05)
    txt(sl, x + Inches(0.35), Inches(1.95), Inches(3.5), Inches(0.35), name, size=17,
        bold=True, color=ORANGE)
    txt(sl, x + Inches(0.35), Inches(2.40), Inches(3.5), Inches(0.28), rol, size=11,
        bold=True, color=WHITE if i == 0 else INK)
    txt(sl, x + Inches(0.35), Inches(2.80), Inches(3.5), Inches(1.7), desc, size=9,
        color=LINE if i == 0 else GRAY, spacing=1.35)
    x += Inches(4.55)
footer(sl)

# ══════════════════════════ 4. EMAIL MARKETING ════════════════════════════════
s_divider(prs, "EMAIL\nMARKETING",
          "Conexiones personalizadas, automatización inteligente y conversiones efectivas. "
          "Descubre cómo el Email Marketing potencia la relación con tus clientes y maximiza "
          "tu retorno.", f"{P}/div_email.jpeg", active="Email M.")

s_split(prs, "Email M.", "¿En qué consiste el", "Email Marketing?",
        body="Es una estrategia de comunicación digital que utiliza el correo electrónico como "
             "canal para promocionar ofertas, informar y mantener contacto directo con los "
             "clientes.",
        items=[("Menos invasivo: ", "permite interactuar con el contenido según la conveniencia "
                "del usuario, mejorando la experiencia con la marca."),
               ("Ofrece métricas de seguimiento: ", "visibilidad y trazabilidad de la "
                "efectividad de las campañas, con KPI de apertura, clics y rebote."),
               ("Fidelización: ", "permite trabajar las bases existentes y potenciar la "
                "contratación recurrente de productos.")],
        photo=f"{P}/laptop_neon.jpeg")

# Beneficios / dato Klaviyo
sl = blank(prs); rect(sl, 0, 0, W, H, fill=WHITE); navbar(sl, active="Email M.")
title2(sl, Inches(0.62), Inches(0.85), "El canal donde", "los flujos mandan", size=23,
       w=Inches(4.5))
txt(sl, Inches(0.62), Inches(1.92), Inches(4.2), Inches(2.2),
    "Los datos de la industria son claros: el valor del email no está en el volumen de "
    "campañas enviadas, sino en los flujos automatizados que reaccionan al comportamiento "
    "de cada usuario.\n\n"
    "Por eso nuestra propuesta prioriza la arquitectura de flujos por sobre la cantidad de "
    "envíos masivos, sin dejar de cumplir la cadencia comprometida.",
    size=9.5, color=GRAY, spacing=1.4)
stats = [("41%", "de los ingresos por email\nlos generan los flujos"),
         ("5,3%", "de los envíos totales\nrepresentan esos flujos"),
         ("5,58%", "click rate de flujos\nvs 1,69% de campañas"),
         ("3,4%", "click rate promedio\nen banca y finanzas")]
x0, y0 = Inches(5.35), Inches(1.35)
cw, chh, g = Inches(2.05), Inches(1.62), Inches(0.18)
for i, (big, small) in enumerate(stats):
    r, c = divmod(i, 2)
    x = x0 + (cw + g) * c
    y = y0 + (chh + g) * r
    first = (i == 0)
    card(sl, x, y, cw, chh, fill=ORANGE if first else RGBColor(0xFA, 0xFA, 0xFA),
         radius=0.08)
    txt(sl, x, y + Inches(0.30), cw, Inches(0.5), big, size=24, bold=True,
        color=WHITE if first else INK, align=PP_ALIGN.CENTER)
    txt(sl, x + Inches(0.12), y + Inches(0.88), cw - Inches(0.24), Inches(0.6), small,
        size=8.2, color=WHITE if first else GRAY_D, align=PP_ALIGN.CENTER, spacing=1.2)
txt(sl, Inches(5.35), Inches(4.82), Inches(4.4), Inches(0.25),
    "Fuente: Klaviyo Benchmarks 2026 (183.000 cuentas) y benchmarks de email por industria.",
    size=7, color=GRAY, italic=True)
footer(sl)

s_numbered(prs, "Email M.", "Estrategia", "y objetivos",
           intro="Metodología de trabajo para construir el programa de email desde cero o "
                 "sobre una base existente.",
           photos=[f"{P}/div_email.jpeg"],
           entries=[("01.", "Definir objetivos",
                     "Objetivos con metodología SMART en base a los resultados deseados para "
                     "las campañas y flujos."),
                    ("02.", "Captación y bases",
                     "Definir cómo se alimentan las bases: publicidad, formularios en el sitio "
                     "y datos propios de la marca."),
                    ("03.", "Herramienta",
                     "Selección de la plataforma según tamaño de lista, funciones de "
                     "automatización, integraciones y requisitos de tratamiento de datos.")])

s_numbered(prs, "Email M.", "Estrategia", "y objetivos",
           intro="Una vez definida la base, el trabajo se concentra en automatizar y medir.",
           photos=[f"{P}/office_wide.jpeg"],
           entries=[("04.", "Contenido",
                     "Definición entre automatización y creación manual de newsletters, con "
                     "línea editorial acorde a la marca."),
                    ("05.", "Automatización",
                     "Implementación de las secuencias que reaccionan al comportamiento del "
                     "usuario en cada etapa del proceso."),
                    ("06.", "Control y optimización",
                     "Medición cíclica de resultados y optimización continua para mejorar la "
                     "eficiencia de la estrategia.")])

# Flujos propuestos
sl = blank(prs); rect(sl, 0, 0, W, H, fill=WHITE); navbar(sl, active="Email M.")
title1(sl, Inches(0.6), Inches(0.80), "Flujos Propuestos", size=23, w=Inches(8.8),
       align=PP_ALIGN.CENTER)
txt(sl, Inches(1.0), Inches(1.28), Inches(8.0), Inches(0.3),
    "Arquitectura de automatizaciones ordenada por valor esperado. Se implementa por fases.",
    size=9.5, color=GRAY, align=PP_ALIGN.CENTER)
flujos = [("Preaprobado sin usar", "Tiene oferta vigente y no la activa. El de mayor retorno."),
          ("Solicitud abandonada", "Inició el proceso y no lo completó."),
          ("Contrato no firmado", "Llegó al final y no firmó. Máxima urgencia."),
          ("Onboarding", "Acompaña al usuario nuevo en los pasos previos a solicitar."),
          ("Nurture educativo", "Historial crediticio y salud financiera para quien no está listo."),
          ("Winback", "Reactivación de bases frías previamente segmentadas."),
          ("Post-contratación", "Cross-sell de otros productos del ecosistema."),
          ("Sunset", "Higiene de lista. Crítico para la entregabilidad con bases antiguas.")]
x0, y0 = Inches(0.42), Inches(1.80)
cw, chh = Inches(2.28), Inches(1.42)
for i, (h, d) in enumerate(flujos):
    r, c = divmod(i, 4)
    x = x0 + (cw + Inches(0.11)) * c
    y = y0 + (chh + Inches(0.17)) * r
    card(sl, x, y, cw, chh, fill=INK if i < 3 else RGBColor(0xFA, 0xFA, 0xFA), radius=0.07)
    txt(sl, x + Inches(0.18), y + Inches(0.18), Inches(0.4), Inches(0.2), f"{i+1:02d}",
        size=9, bold=True, color=ORANGE)
    txt(sl, x + Inches(0.18), y + Inches(0.46), cw - Inches(0.34), Inches(0.3), h,
        size=9.8, bold=True, color=WHITE if i < 3 else INK, spacing=1.1)
    txt(sl, x + Inches(0.18), y + Inches(0.88), cw - Inches(0.34), Inches(0.45), d,
        size=7.8, color=LINE if i < 3 else GRAY, spacing=1.2)
footer(sl)

# ══════════════════════════ 5. DATAPIFY ═══════════════════════════════════════
s_divider(prs, "DATAPIFY",
          "La capa conversacional que opera sobre las campañas: un agente de IA en WhatsApp "
          "que atiende, califica y deriva, disponible las 24 horas.",
          f"{P}/office_vertical.jpeg", active="Datapify")

s_split(prs, "Datapify", "Qué incluye", "Datapify",
        body="Plataforma de automatización conversacional que integramos directamente con las "
             "campañas de Paid Media.",
        items=["Chat IA en WhatsApp disponible 24/7, en español",
               "Búsqueda semántica y comprensión del contexto de la conversación",
               "Segmentos inteligentes que agrupan contactos según su comportamiento",
               "Recuperación automática de procesos abandonados",
               "Agenda de reuniones integrada al calendario",
               "Dashboard con métricas de todas las conversaciones",
               "Campañas con plantillas aprobadas por Meta"],
        photo=f"{P}/div_cm.jpeg", item_size=9.8)

s_text(prs, "Datapify", "Cómo se integra con las campañas",
       sub="Datapify no reemplaza el trabajo de campañas: es el destino al que llegan y el "
           "mecanismo que convierte el clic en un prospecto calificado.",
       items=[("El anuncio abre la conversación. ", "Las campañas Click to WhatsApp de Meta "
               "llevan al usuario directamente al chat, sin formularios intermedios."),
              ("El agente levanta y califica. ", "Recoge la información que la marca defina "
               "como criterio de calificación y resuelve dudas del proceso en tiempo real."),
              ("Deriva solo lo calificado. ", "El área comercial recibe prospectos filtrados "
               "en lugar de volumen sin depurar."),
              ("Recupera lo que se cae. ", "Detecta procesos incompletos y reactiva la "
               "conversación, complementando los flujos de email."),
              ("Opera fuera de horario. ", "La intención de solicitar un crédito no se limita "
               "al horario hábil.")],
       size=9.5)

# ══════════════════════════ 6. MEDICIÓN ═══════════════════════════════════════
sl = blank(prs); rect(sl, 0, 0, W, H, fill=WHITE); navbar(sl, active="Datapify")
title1(sl, Inches(0.6), Inches(0.80), "Medición: eventos a marcar", size=23, w=Inches(8.8),
       align=PP_ALIGN.CENTER)
txt(sl, Inches(0.9), Inches(1.28), Inches(8.2), Inches(0.35),
    "Sin estos eventos, optimizar a \"lead\" genera volumen que el área comercial no cierra. "
    "Medimos hasta el final del embudo.", size=9.5, color=GRAY, align=PP_ALIGN.CENTER)
ev = ["Clic en anuncio", "Conversación iniciada", "Datos de contacto entregados",
      "Prospecto calificado", "Derivación a contratación", "Solicitud iniciada",
      "Solicitud completada", "Contrato firmado", "Crédito cursado",
      "Monto cursado (valor)", "Rechazo y motivo", "Recuperación por flujo"]
x0, y0 = Inches(0.5), Inches(1.90)
cw, chh = Inches(2.28), Inches(0.72)
for i, e in enumerate(ev):
    r, c = divmod(i, 4)
    x = x0 + (cw + Inches(0.12)) * c
    y = y0 + (chh + Inches(0.14)) * r
    hot = i in (3, 8, 9)
    card(sl, x, y, cw, chh, fill=ORANGE if hot else RGBColor(0xF7, 0xF7, 0xF7), radius=0.13)
    txt(sl, x + Inches(0.16), y + Inches(0.245), cw - Inches(0.3), Inches(0.3), e,
        size=9.2, bold=hot, color=WHITE if hot else INK)
txt(sl, Inches(0.5), Inches(4.72), Inches(8.8), Inches(0.3),
    "En naranjo, los tres eventos que consideramos irrenunciables para evaluar el desempeño real.",
    size=8, color=GRAY, italic=True, align=PP_ALIGN.CENTER)
footer(sl)

s_text(prs, "Datapify", "Casos adicionales a evaluar",
       sub="Dejamos planteadas estas preguntas para que el equipo evalúe si corresponde "
           "incorporarlas al alcance de medición. No asumimos respuestas.",
       items=["¿El curse ocurre solo en la app o existen otros canales de contratación que "
              "deban atribuirse a las campañas?",
              "¿Se puede devolver el resultado de la evaluación crediticia a las plataformas "
              "para optimizar hacia prospectos aprobables y no solo hacia volumen?",
              "¿Existe un identificador que permita seguir al prospecto desde el anuncio hasta "
              "el curse sin romper la trazabilidad?",
              "¿Se requiere medir el monto cursado como valor de conversión, o basta el conteo "
              "de operaciones?",
              "¿Hay otros productos del ecosistema — seguros, hipotecario, inversión — que "
              "deban entrar al modelo de atribución?",
              "¿Qué ventana de atribución refleja mejor el ciclo real de decisión de un crédito "
              "de consumo?",
              "¿Se dispone de datos de rechazo y sus motivos para retroalimentar la "
              "segmentación de campañas?"],
       size=9.3)

# ══════════════════════════ 7. CASOS DE ÉXITO ═════════════════════════════════
s_divider(prs, "CASOS\nDE ÉXITO",
          "Resultados que marcan la diferencia. Optimizamos marcas con estrategias en Paid "
          "Media, Community Management y Email Marketing, logrando mayor tráfico, engagement "
          "y conversiones.", f"{P}/office_wide.jpeg", active="Casos Éxito")

s_split(prs, "Casos Éxito", "Caso Paid Media:", "Granja Magdalena",
        body="Briefing: la marca vendía de manera orgánica un promedio de 100 millones de "
             "pesos mensuales antes de la pandemia. Durante la pandemia las ventas subieron a "
             "un promedio de 200 millones mensuales a través del sitio web.\n\n"
             "Desafío: posterior a la pandemia las ventas bajaron a una media de 100 millones "
             "mensuales, por lo que se necesitaba tomar acción para repuntar.",
        items=[("Enfoque: ", "campañas orientadas a conversión, testeando distintos formatos "
                "de anuncios y segmentos hasta encontrar la combinación rentable.")],
        photo=f"{P}/caso_laptop.jpeg")

s_stats(prs, "Casos Éxito", "Resultados Globales", "de Campañas",
        "Durante los meses en que se trabajaron las campañas se implementaron y probaron "
        "diferentes gráficas diseñadas para alinearse con la intención de la marca y las "
        "necesidades específicas de los usuarios. Estos esfuerzos resultaron en las "
        "siguientes métricas.",
        [("21", "ROAS\nPromedio"), ("155.7M", "+49% mensual"),
         ("+31%", "Pedidos\ntotales"), ("+35%", "Sesiones en\ntienda online")],
        photo=f"{P}/office_wide.jpeg", brand="Granja Magdalena")

s_split(prs, "Casos Éxito", "Caso Community M.:", "Inmobiliaria HCG",
        body="Inmobiliaria HCG inició en febrero de 2024 un servicio de Community Management "
             "con el objetivo de optimizar su presencia digital.\n\n"
             "La situación inicial presentaba contenido básico y estándar que no generaba "
             "interacción ni captación de leads. Se estableció como meta mejorar la calidad "
             "del contenido gráfico y audiovisual para atraer leads y aumentar las ventas.",
        items=[("Enfoque: ", "se testearon distintos formatos identificando que los videos y "
                "reels generaban mayor engagement, y se incorporó TikTok reutilizando el "
                "material creado para Instagram.")],
        photo=f"{P}/div_cm.jpeg")

s_stats(prs, "Casos Éxito", "Resultados", "Obtenidos",
        "Desde inicio de año a finales de 2024 la marca logró un crecimiento notable en su "
        "presencia digital. En Instagram los seguidores aumentaron 1.806 de forma orgánica y "
        "el tráfico al perfil creció de 601 a 5.100 visitas mensuales. En TikTok, con solo 18 "
        "publicaciones, se obtuvieron 2.361 nuevos seguidores.",
        [("+2.362%", "Interacción\ndel perfil"), ("+848%", "Actividad\ndel perfil"),
         ("+237%", "Crecimiento\nde seguidores"), ("433K", "Views orgánicas\nde un solo video")],
        photo=f"{P}/office_vertical.jpeg", brand="Inmobiliaria HCG")

s_split(prs, "Casos Éxito", "Caso Email Marketing:", "Rebels Golf",
        body="Briefing: la marca enviaba correos enfocados solo en entregar información o "
             "incentivar visitas a la tienda, dado que no contaba con ecommerce.\n\n"
             "Desafío: trabajar una estrategia comunicacional que mejorara el contenido de los "
             "correos y a la vez lograra ventas a través del nuevo canal digital.",
        items=[("Enfoque: ", "se articuló toda la comunicación bajo un concepto central único "
                "y se desarrollaron contenidos para captar ventas desde el primer envío.")],
        photo=f"{P}/div_email.jpeg")

s_stats(prs, "Casos Éxito", "Resultados Globales", "de la Iniciativa",
        "En septiembre de 2024 se inició el envío de correos para anunciar el nuevo canal y "
        "la estrategia de precios, combinando promociones con servicios en tienda. Se evaluó "
        "el interés mediante tasas de apertura, clics y ventas, y los resultados del trimestre "
        "superaron ampliamente al período anterior.",
        [("+535%", "Ventas\npromedio"), ("+293%", "Aumento ventas\nnoviembre"),
         ("+1256%", "Aumento ventas\noctubre"), ("+57%", "Aumento ventas\nseptiembre")],
        photo=f"{P}/laptop_neon.jpeg", brand="Rebels Golf")

# ══════════════════════════ 8. PROPUESTA DE SERVICIOS ═════════════════════════
s_divider(prs, "PROPUESTA\nDE SERVICIOS",
          "El detalle de lo que incluye cada servicio, su alcance mensual y la forma en que "
          "trabajamos con tu equipo.", f"{P}/laptop_neon.jpeg", active="Propuesta Serv.")

s_spec(prs, "Propuesta Serv.", "Paid Media", "Estrategia y Reportería",
       ["Desarrollo de estrategia mensual para lograr los objetivos definidos",
        "Creación de campañas publicitarias según estrategia y objetivos",
        "Diseño de gráficas y copy para campañas",
        "Monitoreo de campañas y resultados",
        "Reporte mensual de resultados",
        "Comunicación constante con el cliente para nuevas propuestas y mejoras",
        "Optimización de campañas de acuerdo a A/B testing de anuncios y términos de búsqueda"],
       f"{P}/laptop_neon.jpeg", "Paid Media")

s_spec(prs, "Propuesta Serv.", "Paid Media", "Campañas y Data Analytics",
       ["Campañas en base a objetivos de conversión y captación de prospectos calificados",
        "Estructura de campañas en Google Ads y Meta Ads",
        "Campañas Click to WhatsApp integradas al agente conversacional",
        "Retargeting a usuarios que interactuaron sin completar el proceso",
        "Configuración y seguimiento de conversiones",
        "Reportería en Looker Studio",
        "El presupuesto de inversión en campañas es aparte del servicio"],
       f"{P}/div_casos.jpeg", "Paid Media")

s_spec(prs, "Propuesta Serv.", "Community", "Management",
       ["Creación de grilla de contenidos en base a objetivos y fechas relevantes",
        "Creación de contenido y diseño de las publicaciones",
        "2 publicaciones semanales en Instagram (gráfica estática, carrusel o reel)",
        "2 historias diseñadas semanales en Instagram",
        "2 publicaciones semanales en TikTok",
        "Interacción con la comunidad en historias y comentarios",
        "Análisis, reportería y optimización de contenido según resultados",
        "Se trabaja con biblioteca de contenidos o material provisto por la marca"],
       f"{P}/div_cm.jpeg", "Community M.")

s_spec(prs, "Propuesta Serv.", "Email", "Marketing",
       ["Definición de objetivos y estrategia del canal",
        "Selección y configuración de la herramienta de email marketing",
        "Desarrollo de correos para campañas según objetivos",
        "2 correos de campaña semanales, aparte de los flujos automatizados",
        "Implementación de la arquitectura de flujos automatizados",
        "Monitoreo y medición de resultados",
        "Optimización y ajustes para mejorar la eficacia de los correos"],
       f"{P}/div_email.jpeg", "Email M.")

s_spec(prs, "Propuesta Serv.", "Datapify", "Especificaciones",
       ["Chat IA en WhatsApp disponible 24/7",
        "Levantamiento de información, calificación y derivación de prospectos",
        "Búsqueda semántica y comprensión de contexto",
        "Segmentos inteligentes según comportamiento",
        "Recuperación automática de procesos abandonados",
        "Agenda de reuniones integrada",
        "Dashboard con métricas de conversaciones",
        "Campañas con plantillas aprobadas por Meta"],
       f"{P}/office_vertical.jpeg", "Datapify")

s_spec(prs, "Propuesta Serv.", "Servicio", "General",
       ["Atención diaria de 9:00 a 18:00 hrs por WhatsApp, teléfono, correo u otro medio",
        "Creación de grupo de WhatsApp para atención directa",
        "Asignación de equipo dedicado a la cuenta",
        "Reuniones de seguimiento según necesidad",
        "Recomendaciones y comunicación de resultados de forma constante",
        "Desarrollo de servicios adaptados según requerimientos"],
       f"{P}/desk_wide.jpeg", "Servicio")

# ══════════════════════════ 9. PROPUESTA COMERCIAL ════════════════════════════
s_price(prs, [
    ("Paid Media",
     ["Gestión de campañas Google y Meta", "Seguimiento y monitoreo", "Optimización continua",
      "Reportes mensuales", "Looker Studio", "Propuestas de mejora"],
     "35 UF", "6,65 UF", "41,65 UF"),
    ("Community Management",
     ["Grilla de contenidos", "Creación y diseño de contenidos", "Instagram y TikTok",
      "Interacción con la comunidad", "Análisis y reportería"],
     "25 UF", "4,75 UF", "29,75 UF"),
    ("Email Marketing",
     ["Planificación y desarrollo de correos", "2 correos de campaña semanales",
      "Flujos automatizados", "Monitoreo y medición", "Optimización y ajustes"],
     "25 UF", "4,75 UF", "29,75 UF"),
    ("Datapify",
     ["Chat IA en WhatsApp 24/7", "Calificación y derivación", "Segmentos inteligentes",
      "Agenda de reuniones", "Dashboard de métricas"],
     "USD 299", "USD 56,81", "USD 355,81"),
], note="Valores mensuales. Servicios de agencia expresados en UF; Datapify en dólares, "
        "contratado directamente por el cliente con el proveedor. IVA 19%.")

# Resumen de inversión
sl = blank(prs); rect(sl, 0, 0, W, H, fill=WHITE)
rect(sl, 0, Inches(2.55), W, Inches(3.075), fill=INK)
navbar(sl, active="Propuesta Com.")
title1(sl, Inches(0.6), Inches(0.82), "Resumen de Inversión Mensual", size=25, w=Inches(8.8),
       align=PP_ALIGN.CENTER)
txt(sl, Inches(1.2), Inches(1.34), Inches(7.6), Inches(0.3),
    "Servicios de agencia. La inversión en medios se detalla en el Plan de Medios adjunto.",
    size=9.5, color=GRAY, align=PP_ALIGN.CENTER)
card(sl, Inches(1.35), Inches(1.78), Inches(7.3), Inches(2.72), fill=WHITE, radius=0.045)
rows = [("Paid Media", "35 UF", "6,65 UF", "41,65 UF"),
        ("Community Management", "25 UF", "4,75 UF", "29,75 UF"),
        ("Email Marketing", "25 UF", "4,75 UF", "29,75 UF")]
hy = Inches(2.02)
txt(sl, Inches(1.62), hy, Inches(2.2), Inches(0.22), "Servicio", size=8.5, bold=True,
    color=GRAY)
for j, h in enumerate(["Valor", "IVA", "Total"]):
    txt(sl, Inches(4.04) + Inches(1.42) * j, hy, Inches(1.4), Inches(0.22), h, size=8.5,
        bold=True, color=GRAY, align=PP_ALIGN.RIGHT)
rect(sl, Inches(1.62), Inches(2.30), Inches(6.76), Pt(1), fill=LINE)
for i, (n, v, iv, t) in enumerate(rows):
    y = Inches(2.44) + Inches(0.42) * i
    txt(sl, Inches(1.62), y, Inches(2.6), Inches(0.25), n, size=10.5, color=INK)
    for j, val in enumerate([v, iv, t]):
        txt(sl, Inches(4.04) + Inches(1.42) * j, y, Inches(1.4), Inches(0.25), val,
            size=10.5, bold=(j == 2), color=INK, align=PP_ALIGN.RIGHT)
rect(sl, Inches(1.62), Inches(3.82), Inches(6.76), Pt(1.4), fill=ORANGE)
txt(sl, Inches(1.62), Inches(3.98), Inches(2.6), Inches(0.3), "TOTAL SERVICIOS", size=11.5,
    bold=True, color=INK)
for j, val in enumerate(["85 UF", "16,15 UF", "101,15 UF"]):
    txt(sl, Inches(4.04) + Inches(1.42) * j, Inches(3.98), Inches(1.4), Inches(0.3), val,
        size=11.5, bold=True, color=ORANGE if j == 2 else INK, align=PP_ALIGN.RIGHT)
txt(sl, Inches(1.35), Inches(4.60), Inches(7.3), Inches(0.25),
    "Datapify: USD 299 + IVA mensual, contratado directamente por el cliente con el proveedor.",
    size=8.5, color=LINE, align=PP_ALIGN.CENTER)
txt(sl, Inches(1.35), Inches(4.90), Inches(7.3), Inches(0.3),
    "Inversión en medios recomendada: $3.000.000 - $5.000.000 CLP mensuales, "
    "pagados directamente a cada plataforma.", size=8.5, color=ORANGE_2,
    align=PP_ALIGN.CENTER)
footer(sl, dark=True)

# ══════════════════════════ 10. CONDICIONES COMERCIALES ═══════════════════════
COND = [
 ("Vigencia y naturaleza de la propuesta",
  "Esta propuesta tiene una vigencia de 30 días corridos desde su emisión. En esta etapa "
  "constituye una estimación referencial y no vinculante."),
 ("Moneda y reajuste",
  "Los valores de los servicios se expresan en UF y se facturan en pesos al valor de la UF "
  "del día de emisión de la factura. Datapify se expresa en dólares."),
 ("Condiciones de pago",
  "Facturación mensual anticipada. El pago se realiza dentro de los días acordados desde la "
  "recepción de la factura."),
 ("Plazo mínimo sugerido",
  "Se sugiere un plazo mínimo de 6 meses. El fundamento es técnico: las campañas de "
  "conversión requieren volumen de eventos para completar su fase de aprendizaje."),
 ("Aviso de término",
  "Cualquiera de las partes puede poner término al servicio con 30 días de aviso previo por "
  "escrito."),
 ("Mes de implementación",
  "El primer mes contempla configuración, medición y puesta en marcha. Los resultados "
  "comparables se leen a partir del segundo o tercer mes."),
 ("Presupuesto de medios",
  "El presupuesto de inversión publicitaria es aparte del valor del servicio y se paga "
  "directamente a cada plataforma."),
 ("Titularidad de cuentas y datos",
  "Las cuentas publicitarias, la plataforma de email y las herramientas asociadas quedan a "
  "nombre del cliente. La agencia accede como usuario autorizado."),
 ("Licencias de terceros",
  "Las licencias de plataformas de terceros no están incluidas en el valor del servicio y son "
  "contratadas directamente por el cliente."),
 ("Provisión de contenido",
  "El servicio no incluye grabación ni producción audiovisual en terreno. Se trabaja con "
  "biblioteca de contenidos o material provisto por la marca."),
 ("Plazo de aprobación de piezas",
  "El cliente dispone de 48 horas hábiles para aprobar u observar las piezas enviadas. Los "
  "plazos de publicación se ajustan según los tiempos de respuesta."),
 ("Validación legal de las piezas",
  "El cliente valida las tasas, condiciones y textos legales publicados. La agencia no "
  "responde por la exactitud de la información financiera entregada por la marca."),
 ("Confidencialidad",
  "Ambas partes se obligan a mantener reserva sobre la información intercambiada durante la "
  "relación comercial."),
]
for page in range(0, len(COND), 5):
    grupo = COND[page:page + 5]
    sl = blank(prs); rect(sl, 0, 0, W, H, fill=WHITE); navbar(sl, active="Propuesta Com.")
    accent_arrow(sl, Inches(0.46), Inches(0.95))
    title1(sl, Inches(0.72), Inches(0.88), "Condiciones Comerciales", size=23, w=Inches(6.5))
    txt(sl, Inches(7.6), Inches(0.98), Inches(1.8), Inches(0.3),
        f"{page//5 + 1} / {(len(COND)+4)//5}", size=10, color=GRAY, align=PP_ALIGN.RIGHT)
    y = Inches(1.68)
    for i, (h, d) in enumerate(grupo):
        n = page + i + 1
        pill(sl, Inches(0.72), y + Inches(0.02), Inches(0.36), Inches(0.28), f"{n:02d}",
             size=9, radius=False)
        txt(sl, Inches(1.22), y, Inches(7.9), Inches(0.25), h, size=11, bold=True, color=INK)
        txt(sl, Inches(1.22), y + Inches(0.28), Inches(7.9), Inches(0.42), d, size=9,
            color=GRAY, spacing=1.3)
        y += Inches(0.70)
    footer(sl)

s_contact(prs)
prs.save(OUT)
print("Láminas totales:", len(prs.slides._sldIdLst))
print("Guardado:", OUT)
