# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/tmp/claude-0/-home-user-meta-mcp/3417b367-2cff-5bc9-8662-cddb20c827cd/scratchpad")
import deck_lib
deck_lib.NAV = ["Contexto", "Cliente", "Regulación", "Paid Media", "Email M.", "Social",
                "Inversión"]
from deck_lib import *
import slides
slides.NAV = deck_lib.NAV
from slides import *
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

OUT = "/home/user/meta-mcp/propuesta-dale-coopeuch/04_Investigacion_de_Mercado_Resumen.pptx"
prs = new_deck()
P = PHOTO

# 1. Portada
sl = blank(prs); rect(sl, 0, 0, W, H, fill=BLACK)
picture_cover(sl, f"{P}/caso_laptop.jpeg", Inches(-0.35), Inches(0.35), Inches(5.7),
              Inches(4.9))
x = Inches(5.05)
txt(sl, x, Inches(0.85), Inches(4.7), Inches(0.9), "INVESTIGACIÓN", size=36, bold=True,
    color=ORANGE)
txt(sl, x, Inches(1.55), Inches(4.7), Inches(0.7), "DE MERCADO", size=27, bold=True,
    color=WHITE)
txt(sl, x, Inches(2.35), Inches(4.7), Inches(0.6), "Dale Coopeuch", size=22, color=WHITE)
txt(sl, x, Inches(3.15), Inches(4.6), Inches(0.8),
    "Benchmarks e insights para la estrategia de canales digitales\n"
    "Resumen ejecutivo · Agosto 2026", size=9.5, color=LINE, spacing=1.4)
pill(sl, x, Inches(4.12), Inches(1.62), Inches(0.36), "Comenzar  →", size=9.5)
footer(sl, dark=True)

# 2. Alcance
s_text(prs, "Contexto", "Qué contiene este documento",
       sub="Resumen del informe detallado que se entrega por separado. Todas las cifras están "
           "atribuidas a su fuente y fecha.",
       items=[("Fuentes públicas verificables. ", "Documentación oficial de plataformas, "
               "estadísticas de la CMF, reportes de inversión de AAM e IAB Chile y estudios de "
               "benchmark de la industria."),
              ("Sin acceso a las cuentas del cliente. ", "Todas las métricas de desempeño son "
               "referencias externas, no mediciones del anunciante."),
              ("Los benchmarks internacionales no se trasladan en valor absoluto. ", "Se usan "
               "como referencia de la relación entre métricas. El valor en pesos se triangula "
               "con fuentes locales."),
              ("Donde no hay dato confiable, se declara. ", "No se rellenan vacíos con "
               "estimaciones sin respaldo.")],
       size=9.8)

# 3. Los seis hallazgos
sl = blank(prs); rect(sl, 0, 0, W, H, fill=WHITE); navbar(sl, active="Contexto")
title1(sl, Inches(0.6), Inches(0.80), "Seis hallazgos que ordenan la estrategia", size=22,
       w=Inches(8.8), align=PP_ALIGN.CENTER)
hall = [("El problema no es tráfico", "Es la fricción del proceso de contratación. Cada paso "
         "es un punto de fuga que hoy no se mide por separado."),
        ("Hay un diferenciador sin ocupar", "La evaluación por múltiples fuentes de ingreso "
         "habilita el nicho de independientes. Nadie lo comunica."),
        ("La landing no cumple con Google", "No expone CAE, plazos ni costo total. Es un "
         "bloqueante previo al lanzamiento."),
        ("En Chile sí hay segmentación en Meta", "Las restricciones de categoría especial "
         "aplican a EE.UU., Canadá y parte de Europa. Chile no."),
        ("En email mandan los flujos", "41% de los ingresos con 5,3% de los envíos. Banca "
         "tiene el click rate más bajo de todas las industrias."),
        ("En social hay que fijar el objetivo correcto", "Engagement estructuralmente bajo en "
         "finanzas. El rol es confianza, no seguidores.")]
x0, y0 = Inches(0.42), Inches(1.50)
cw, chh = Inches(3.06), Inches(1.72)
for i, (h, d) in enumerate(hall):
    r, c = divmod(i, 3)
    x = x0 + (cw + Inches(0.11)) * c
    y = y0 + (chh + Inches(0.16)) * r
    card(sl, x, y, cw, chh, fill=INK if i in (1, 2, 3) else RGBColor(0xFA, 0xFA, 0xFA),
         radius=0.06)
    txt(sl, x + Inches(0.20), y + Inches(0.18), Inches(0.4), Inches(0.2), f"{i+1:02d}",
        size=9.5, bold=True, color=ORANGE)
    txt(sl, x + Inches(0.20), y + Inches(0.46), cw - Inches(0.4), Inches(0.4), h, size=10.5,
        bold=True, color=WHITE if i in (1, 2, 3) else INK, spacing=1.15)
    txt(sl, x + Inches(0.20), y + Inches(0.98), cw - Inches(0.4), Inches(0.65), d, size=8.2,
        color=LINE if i in (1, 2, 3) else GRAY, spacing=1.25)
footer(sl)

# 4. Contexto de mercado
s_stats(prs, "Contexto", "El contexto", "de mercado",
        "La cartera de consumo es el corazón del negocio cooperativo y lo digital ya superó la "
        "mitad de la inversión publicitaria chilena. Al mismo tiempo, los indicadores de riesgo "
        "de la cartera de consumo muestran alzas, lo que refuerza la necesidad de calificar "
        "antes de derivar.",
        [("68,7%", "de la cartera de\ncooperativas es consumo"),
         ("+4,77%", "crecimiento real\na doce meses"),
         ("50,1%", "share de inversión\ndigital en Chile"),
         ("+213%", "crecimiento del uso\nde tarjetas prepago")],
        photo=f"{P}/div_casos.jpeg")

# 5. Competencia
s_split(prs, "Cliente", "Dale compite", "en dos canchas",
        body="La estrategia de comunicación no puede tratar ambas como una sola.",
        items=[("Cuenta y prepago: ", "Tenpo, MACH, Mercado Pago y Tapp, todas sin costo de "
                "mantención. Mercado Pago entra a crédito en 2026 y Tenpo busca ser el primer "
                "neobanco del país."),
               ("Crédito de consumo: ", "banca, cooperativas y retail financiero. Es la cancha "
                "donde está el objetivo declarado."),
               ("La ventaja estructural: ", "el Remanente. La devolución anual de utilidades al "
                "Socio no tiene equivalente en ningún neobanco.")],
        photo=f"{P}/office_wide.jpeg")

# 6. El embudo
s_numbered(prs, "Cliente", "El embudo", "hacia el curse",
           intro="Cada etapa es un punto de fuga medible. Con un embudo de esta longitud, "
                 "optimizar hacia \"lead\" produce volumen que no se traduce en curse.",
           photos=[f"{P}/office_vertical.jpeg", f"{P}/desk_wide.jpeg"],
           entries=[("01.", "Impacto y conversación",
                     "El anuncio deriva a WhatsApp. Iniciar una conversación exige menos "
                     "compromiso que completar un formulario en frío."),
                    ("02.", "Calificación y derivación",
                     "El agente IA levanta información y filtra. El área comercial recibe "
                     "prospectos depurados, no volumen bruto."),
                    ("03.", "Contratación y curse",
                     "Requisitos previos, evaluación en línea, monto y firma. Los flujos "
                     "automatizados recuperan a quien no completa.")])

# 7. Diferenciador
s_split(prs, "Cliente", "El diferenciador", "que no se está usando",
        body="Textual del sitio: \"Te evaluamos con inteligencia financiera en tiempo real "
             "considerando múltiples fuentes de ingreso\".",
        items=[("Abre un nicho amplio y desatendido. ", "Trabajadores independientes, "
                "honorarios y de plataformas, sistemáticamente rechazados por la evaluación "
                "tradicional que exige liquidación de sueldo."),
               ("Ningún competidor directo lo comunica. ", "Es territorio libre en el mensaje "
                "publicitario."),
               ("Hoy está enterrado. ", "Aparece en el cuerpo de una landing, no como eje de "
                "comunicación.")],
        photo=f"{P}/div_cm.jpeg")

# 8. Regulación Google
s_text(prs, "Regulación", "Google exige divulgar el costo del crédito",
       sub="Requisito de política para anuncios de préstamos personales. Sistema de faltas: a "
           "la tercera, suspensión de cuenta.",
       items=[("Debe mostrarse de forma destacada en la landing o la app: ", "período mínimo y "
               "máximo de pago, CAE máxima y un ejemplo representativo del costo total "
               "incluidas todas las comisiones."),
              ("Regla de los 61 días. ", "Solo se permiten préstamos con pago íntegro en 61 "
               "días o más."),
              ("Hallazgo verificado: la landing de Dale no lo cumple hoy. ", "Se revisó "
               "dalecoopeuch.cl/creditodigital a nivel de código fuente. No aparece CAE, ni "
               "tasa, ni plazos, ni montos, ni costo total, ni ejemplo representativo."),
              ("Es un bloqueante previo al lanzamiento. ", "Debe resolverse antes de activar "
               "campañas de búsqueda hacia esa URL.")],
       size=9.8)

# 9. Regulación Meta
s_text(prs, "Regulación", "En Chile conservamos la segmentación de Meta",
       sub="Una buena noticia que conviene verificar antes de dar por perdidas las audiencias "
           "avanzadas.",
       items=[("La categoría especial de crédito restringe fuerte. ", "Desactiva audiencias "
               "similares, impide exclusiones de segmentación detallada y limita la "
               "segmentación geográfica."),
              ("Pero su alcance es EE.UU., Canadá y parte de Europa. ", "Chile no figura en "
               "ese alcance según la documentación de Meta."),
              ("En consecuencia: ", "para campañas dirigidas a Chile se conservan audiencias "
               "personalizadas, lookalikes y segmentación detallada."),
              ("Lo que sí aplica siempre: ", "segmentación 18+ obligatoria, posible "
               "verificación del anunciante con acreditación regulatoria y prohibición de "
               "solicitar datos sensibles dentro de la pieza."),
              ("Revisar al implementar. ", "Meta ha ampliado este alcance de forma progresiva.")],
       size=9.5)


# 10. Benchmarks tabla — Google y Meta
def bench_table(sl, x, y, w, headers, rows, colw):
    hy = y
    for j, h in enumerate(headers):
        txt(sl, x + Inches(sum(colw[:j])), hy, Inches(colw[j]), Inches(0.22), h, size=8,
            bold=True, color=GRAY, align=PP_ALIGN.LEFT if j == 0 else PP_ALIGN.RIGHT)
    rect(sl, x, hy + Inches(0.26), w, Pt(1), fill=LINE)
    for i, row in enumerate(rows):
        ry = hy + Inches(0.38 + 0.30 * i)
        for j, v in enumerate(row):
            txt(sl, x + Inches(sum(colw[:j])), ry, Inches(colw[j]), Inches(0.24), v,
                size=8.8, bold=(j == 1), color=INK if j < 2 else GRAY,
                align=PP_ALIGN.LEFT if j == 0 else PP_ALIGN.RIGHT)

sl = blank(prs); rect(sl, 0, 0, W, H, fill=WHITE); navbar(sl, active="Paid Media")
title1(sl, Inches(0.6), Inches(0.82), "Benchmarks de Paid Media", size=23, w=Inches(8.8),
       align=PP_ALIGN.CENTER)
txt(sl, Inches(1.0), Inches(1.30), Inches(8.0), Inches(0.3),
    "Referencias internacionales. El patrón importa más que el valor absoluto.",
    size=9.5, color=GRAY, align=PP_ALIGN.CENTER)
txt(sl, Inches(0.6), Inches(1.78), Inches(4.2), Inches(0.25), "GOOGLE ADS", size=10,
    bold=True, color=ORANGE)
bench_table(sl, Inches(0.6), Inches(2.12), Inches(4.05),
            ["Métrica", "Finanzas", "Banca"],
            [["CPC Search", "USD 3,46", "USD 3,08"],
             ["CTR Search", "8,3%", "3,41%"],
             ["Conversión", "2,5%", "4,72%"],
             ["CPA Search", "—", "USD 65,25"],
             ["CPC interanual", "—", "+10%"]],
            [1.75, 1.15, 1.15])
txt(sl, Inches(5.35), Inches(1.78), Inches(4.2), Inches(0.25), "META ADS", size=10,
    bold=True, color=ORANGE)
bench_table(sl, Inches(5.35), Inches(2.12), Inches(4.05),
            ["Métrica", "Valor", "Campaña"],
            [["CPC finanzas", "USD 3,77", "conversión"],
             ["CPC finanzas", "USD 1,22", "tráfico"],
             ["CTR esperable", "0,7 - 1,0%", "vertical B2B"],
             ["Conversión", "9,09%", "finanzas"],
             ["CPM alto costo", "> USD 20", "señal"]],
            [1.75, 1.15, 1.15])
card(sl, Inches(0.6), Inches(4.02), Inches(8.8), Inches(0.78), fill=RGBColor(0xFD, 0xF0, 0xE4),
     radius=0.12)
txt(sl, Inches(0.88), Inches(4.18), Inches(8.3), Inches(0.5),
    [("El patrón: ", {"bold": True, "color": ORANGE}),
     ("finanzas tiene CTR alto y conversión baja. La gente hace clic con facilidad, compara "
      "proveedores y duda antes de entregar datos personales. Ese es exactamente el problema "
      "que la conversación asistida resuelve.", {"color": INK})], size=9, spacing=1.3)
txt(sl, Inches(0.6), Inches(4.94), Inches(8.8), Inches(0.2),
    "Fuente: WordStream 2026, Digital Applied Q1 2026 y benchmarks de Meta Ads por industria 2026.",
    size=7, color=GRAY, italic=True, align=PP_ALIGN.CENTER)
footer(sl)

# 11. Triangulación CPC
sl = blank(prs); rect(sl, 0, 0, W, H, fill=WHITE); navbar(sl, active="Inversión")
title2(sl, Inches(0.62), Inches(0.85), "Triangulación del CPC", "para el mercado chileno",
       size=22, w=Inches(4.5))
txt(sl, Inches(0.62), Inches(1.90), Inches(4.2), Inches(2.4),
    "No existe una fuente única y autorizada de CPC por industria para Chile. Para llegar a "
    "una banda defendible se cruzaron dos vías independientes que no se citan entre sí.\n\n"
    "Ambas convergen en la misma zona. Ese solapamiento es lo que da validez al número: Chile "
    "se sitúa en torno al 60% a 80% del CPC estadounidense en esta industria, no en la "
    "fracción mucho menor que suele asumirse.", size=9.5, color=GRAY, spacing=1.4)
tri = [("A", "Benchmark EE.UU. convertido", "$2.807 - $3.154", False),
       ("B", "Reportes locales Chile", "$2.000 - $3.000", False),
       ("=", "Banda triangulada de trabajo", "$2.400 - $3.200", True)]
y = Inches(1.55)
for tag, label, val, hot in tri:
    card(sl, Inches(5.30), y, Inches(4.1), Inches(0.95), fill=ORANGE if hot else
         RGBColor(0xFA, 0xFA, 0xFA), radius=0.10)
    txt(sl, Inches(5.52), y + Inches(0.16), Inches(0.4), Inches(0.25), tag, size=11,
        bold=True, color=WHITE if hot else ORANGE)
    txt(sl, Inches(5.95), y + Inches(0.16), Inches(3.2), Inches(0.25), label, size=9,
        color=WHITE if hot else GRAY_D)
    txt(sl, Inches(5.95), y + Inches(0.44), Inches(3.2), Inches(0.32), val + " CLP",
        size=15, bold=True, color=WHITE if hot else INK)
    y += Inches(1.10)
txt(sl, Inches(5.30), Inches(4.92), Inches(4.1), Inches(0.2),
    "Dólar observado $911,43 al 26-ago-2026.", size=7, color=GRAY, italic=True)
footer(sl)

# 12. Email
sl = blank(prs); rect(sl, 0, 0, W, H, fill=WHITE); navbar(sl, active="Email M.")
title2(sl, Inches(0.62), Inches(0.85), "En email", "mandan los flujos", size=23, w=Inches(4.5))
txt(sl, Inches(0.62), Inches(1.92), Inches(4.2), Inches(2.3),
    "El 5,3% de los envíos produce el 41% de los ingresos. Un programa que solo envía campañas "
    "masivas deja fuera la parte del canal que efectivamente convierte.\n\n"
    "Banca y finanzas presenta además la tasa de clic más baja de todas las industrias "
    "medidas. Conviene declararlo desde el inicio en lugar de que el cliente lo descubra al "
    "tercer mes comparándose contra benchmarks de retail.", size=9.5, color=GRAY, spacing=1.4)
st = [("41%", "de los ingresos por email\nlos generan los flujos"),
      ("5,3%", "de los envíos totales\nrepresentan esos flujos"),
      ("13x", "tasa de pedido de flujos\nsobre campañas"),
      ("3,4%", "click rate promedio\nen banca y finanzas")]
x0, y0 = Inches(5.35), Inches(1.35)
cw, chh, g = Inches(2.05), Inches(1.62), Inches(0.18)
for i, (big, small) in enumerate(st):
    r, c = divmod(i, 2)
    x = x0 + (cw + g) * c; y = y0 + (chh + g) * r
    first = (i == 0)
    card(sl, x, y, cw, chh, fill=ORANGE if first else RGBColor(0xFA, 0xFA, 0xFA), radius=0.08)
    txt(sl, x, y + Inches(0.30), cw, Inches(0.5), big, size=24, bold=True,
        color=WHITE if first else INK, align=PP_ALIGN.CENTER)
    txt(sl, x + Inches(0.12), y + Inches(0.88), cw - Inches(0.24), Inches(0.6), small,
        size=8.2, color=WHITE if first else GRAY_D, align=PP_ALIGN.CENTER, spacing=1.2)
txt(sl, Inches(5.35), Inches(4.82), Inches(4.4), Inches(0.25),
    "Fuente: Klaviyo Benchmarks 2026, sobre más de 183.000 cuentas.", size=7, color=GRAY,
    italic=True)
footer(sl)

# 13. Social
s_grid(prs, "Social", "Engagement en servicios financieros",
       [("Instagram · 0,26% - 0,67%", "Muy por debajo del promedio general. Educación superior "
         "alcanza 2,10% en la misma plataforma."),
        ("TikTok · 1,9%", "Entre 3 y 10 veces el rendimiento de Instagram en prácticamente "
         "toda industria medida."),
        ("Facebook · en retroceso", "El sector registra crecimiento negativo de seguidores, "
         "-0,61% semanal."),
        ("El objetivo correcto", "Con tasas estructuralmente bajas, prometer crecimiento de "
         "comunidad sería vender una métrica que la industria no entrega. El rol del contenido "
         "es reducir desconfianza y explicar el proceso.")],
       cols=4, sub="Fuente: Rival IQ y estudios agregados de benchmarks sociales, 2026")

# 14. Keywords
s_text(prs, "Paid Media", "Arquitectura de palabras clave",
       sub="Sin acceso a la cuenta no es posible entregar volúmenes reales. Se propone la "
           "estructura, lista para dimensionar con Keyword Planner en la primera semana.",
       items=[("Grupo Marca. ", "dale coopeuch · credito dale coopeuch · credito digital dale. "
               "Prioridad alta, costo bajo, rol defensivo."),
              ("Grupo Genérico Crédito. ", "credito de consumo online · solicitar credito "
               "online · credito sin ir al banco · simular credito de consumo. Prioridad alta, "
               "costo alto."),
              ("Grupo Inclusión Financiera. ", "credito para independientes · credito sin "
               "liquidacion de sueldo · credito para trabajadores a honorarios. El grupo "
               "diferencial de la cuenta."),
              ("Negativas obligatorias. ", "hipotecario y automotriz · informacionales puras · "
               "búsqueda de empleo · gestión de cuenta existente · términos de riesgo "
               "reputacional."),
              ("Criterio de estructura. ", "Un grupo por intención, no por producto. Cada uno "
               "requiere mensaje y landing distintos.")],
       size=9.5)

# 15. Modelo de inversión
sl = blank(prs); rect(sl, 0, 0, W, H, fill=WHITE)
rect(sl, 0, Inches(2.62), W, Inches(3.005), fill=INK)
navbar(sl, active="Inversión")
title1(sl, Inches(0.6), Inches(0.82), "Modelo de inversión", size=24, w=Inches(8.8),
       align=PP_ALIGN.CENTER)
txt(sl, Inches(1.0), Inches(1.32), Inches(8.0), Inches(0.3),
    "Construido de abajo hacia arriba desde el costo por clic triangulado. Escenario de "
    "$3.500.000 CLP mensuales.", size=9.5, color=GRAY, align=PP_ALIGN.CENTER)
res = [("~2.970", "clics\nestimados"), ("~678", "conversaciones\niniciadas"),
       ("~237", "prospectos\ncalificados"), ("~47", "cursos\nestimados")]
x0 = Inches(0.55)
for i, (big, small) in enumerate(res):
    x = x0 + Inches(2.28) * i
    card(sl, x, Inches(1.82), Inches(2.12), Inches(1.42),
         fill=ORANGE if i == 3 else WHITE, radius=0.09)
    txt(sl, x, Inches(2.05), Inches(2.12), Inches(0.45), big, size=21, bold=True,
        color=WHITE if i == 3 else INK, align=PP_ALIGN.CENTER)
    txt(sl, x + Inches(0.1), Inches(2.60), Inches(1.92), Inches(0.5), small, size=8.5,
        color=WHITE if i == 3 else GRAY_D, align=PP_ALIGN.CENTER, spacing=1.2)
duo = [("~$14.800", "Costo por prospecto calificado"), ("~$74.500", "Costo por curse")]
for i, (big, small) in enumerate(duo):
    x = Inches(1.55) + Inches(3.5) * i
    txt(sl, x, Inches(3.62), Inches(3.4), Inches(0.5), big + " CLP", size=22, bold=True,
        color=ORANGE, align=PP_ALIGN.CENTER)
    txt(sl, x, Inches(4.14), Inches(3.4), Inches(0.3), small, size=9.5, color=WHITE,
        align=PP_ALIGN.CENTER)
txt(sl, Inches(0.6), Inches(4.62), Inches(8.8), Inches(0.4),
    "No es una promesa de resultado: es la explicitación del razonamiento detrás de la "
    "inversión recomendada de $3.000.000 a $5.000.000 CLP mensuales. La tasa de aprobación a "
    "curse es el único supuesto que debe aportar el cliente.", size=8.5, color=LINE,
    align=PP_ALIGN.CENTER, spacing=1.3)
footer(sl, dark=True)

# 16. Conclusiones
s_text(prs, "Inversión", "Qué hacer antes de invertir el primer peso",
       sub="Cuatro definiciones previas que condicionan el lanzamiento.",
       items=[("Resolver la divulgación de condiciones del crédito. ", "Publicar CAE, plazos, "
               "montos y ejemplo representativo del costo total en la landing pública. Es "
               "requisito de Google Ads."),
              ("Definir el mapa de eventos y su medición. ", "Sin trazabilidad hasta el curse, "
               "la optimización trabajará sobre la métrica equivocada."),
              ("Confirmar la tasa de aprobación crediticia. ", "Es el único parámetro del "
               "modelo que no puede estimarse desde fuentes externas."),
              ("Verificar los requisitos de verificación del anunciante. ", "Tanto en Google "
               "como en Meta, antes de programar el lanzamiento."),
              ("Y las tres métricas que definen el éxito: ", "costo por prospecto calificado, "
               "tasa de aprobación de los derivados y costo por curse.")],
       size=9.5)

s_contact(prs)
prs.save(OUT)
print("Láminas:", len(prs.slides._sldIdLst), "→", OUT)
