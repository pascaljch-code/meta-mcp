# Diagnóstico: síntoma → causas ordenadas por probabilidad

Método: para cada síntoma, recorre las causas en orden y **descarta con evidencia** antes de pasar a la siguiente.
No apliques dos correcciones a la vez o no sabrás cuál funcionó.

## Las conversiones cayeron a 0 (o casi)

1. **Tag roto / deploy del sitio** → probar conversión end-to-end hoy mismo; revisar "Estado de conversión".
2. **Banner de consentimiento** cambiado y bloqueando el tag antes del consentimiento.
3. **Landing con formulario roto** o thank-you page sin evento (probar en móvil, no solo desktop).
4. **Campaña pausada / rechazada / tarjeta rechazada**.
5. Caída real de demanda (verificar con Google Trends y con el resto de canales del cliente).

## CPL bruto bajo pero cero ventas / leads basura

1. **Conversión primaria mal elegida** (optimiza a formulario, no a lead calificado) → Fase 2.
2. **Términos de búsqueda de intención ajena** (curiosidad, "gratis", arriendo vs. venta, otra ciudad) → negativos.
3. **PMax/AI Max fugando gasto** a Display/YouTube o a consultas amplias → reporte por canal, temas de
   búsqueda, negativos, exclusiones de marca.
4. **Formulario sin preguntas calificadoras** (agregar 1–2: presupuesto, plazo, financiamiento aprobado).
5. **Oferta de la landing demasiado blanda** ("recibe información") atrae a todos → endurecer la promesa.
6. **Geo por interés en lugar de presencia** → cambiar a "presencia" en configuración de ubicación.

## CPL alto / CPA fuera de objetivo

1. **Objetivo mal calibrado** contra el rendimiento real (ver cambio del 17-ago-2026 en `escalado.md`).
2. **Aprendizaje permanente** por volumen insuficiente → consolidar campañas y ad groups.
3. **CVR de landing baja** con CTR normal → problema de landing, no de tráfico. Compara CVR por dispositivo.
4. **Competencia**: Auction Insights, CPC al alza, nuevos entrantes → decidir pelear o reubicar presupuesto.
5. **Cobertura de intención pobre**: solo términos genéricos caros; falta la cola media específica.
6. **Canibalización de marca**: PMax o genérico comprando marca y encareciendo lo que ya era gratis.
7. **Horario/dispositivo** con rendimiento dispar y sin ajuste.

## ROAS bajo (ecommerce)

1. **Valor de conversión = ingreso bruto** en lugar de margen → decisiones sesgadas hacia productos malos.
2. **Feed pobre** (títulos, atributos, imágenes) → es la palanca nº1 antes de tocar pujas.
3. **Mix de marca vs. no-marca** inflando el ROAS aparente.
4. **PMax comiéndose la búsqueda de marca** → exclusiones de marca.
5. **Devoluciones** no descontadas de la señal.
6. **AOV o stock** cambiados sin re-calibrar tROAS.

## Volumen estancado con buen CPA

Ya no es problema de eficiencia, es de **techo de demanda**: pasa al orden de escalado
(`escalado.md` §Orden) — destrabar presupuesto, ampliar intención, geo, aflojar objetivo, sumar formato.

## Leads buenos que no cierran

Cuello de botella comercial, no publicitario. Evidencia: % de leads contactados, tiempo al primer contacto,
nº de intentos. Si el SLA supera los 5 minutos en horario hábil, se documenta en el reporte y **no** se
compensa con más presupuesto.

## Benchmarks: cómo usarlos

- La referencia válida es **la línea base de la propia cuenta** (últimos 90 días antes de tu gestión).
- Referencias externas 2026 solo para sanidad de orden de magnitud: CPL mezclado en inmobiliaria de
  operadores con buen desempeño ~USD 18–55 según mercado y ticket; landings dedicadas convierten ~2,4×
  mejor que páginas genéricas; remarketing baja el CPL 20–40%.
- Nunca prometas un benchmark externo como objetivo del cliente. El objetivo se deriva de su economía:
  ticket × margen × tasa de cierre.
