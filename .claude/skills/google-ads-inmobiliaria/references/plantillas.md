# Plantillas

## 1. Reporte mensual (cliente)

```
CUENTA: ____________________   MES: ______   FASE: __   GESTOR: ______

1. RESULTADO
| Métrica                  | Mes actual | Mes anterior | Objetivo | Δ |
|--------------------------|-----------|--------------|----------|---|
| Inversión                |           |              |          |   |
| Leads (total)            |           |              |          |   |
| Leads calificados        |           |              |          |   |
| % calificados            |           |              |          |   |
| CPL bruto                |           |              |          |   |
| CPL calificado           |           |              |          |   |
| Visitas agendadas        |           |              |          |   |
| Reservas / ventas        |           |              |          |   |
| ROAS / ROI               |           |              |          |   |
(ecommerce: reemplazar leads por pedidos, AOV, ROAS, margen)

2. CUELLO DE BOTELLA DEL MES
   [ ] Tráfico   [ ] Landing   [ ] Calidad de lead   [ ] Seguimiento comercial
   Evidencia: ______________________________________________

3. QUÉ HICIMOS (máx. 5 acciones con su efecto medido)

4. QUÉ HAREMOS EL MES QUE VIENE (3 prioridades, no más)

5. DECISIÓN DE PRESUPUESTO
   Actual: ____  Propuesto: ____  (+__%)  Justificación: ____________

6. LO QUE NECESITAMOS DEL CLIENTE
   (ej. SLA de contacto, fotos del proyecto, precios actualizados, acceso al CRM)
```

## 2. Log de cambios (obligatorio)

```
| Fecha | Cuenta | Campaña | Cambio | Hipótesis | Métrica a vigilar | Revisar el | Resultado |
|-------|--------|---------|--------|-----------|-------------------|-----------|-----------|
```

Sin fecha de revisión, un cambio no está terminado. Sin hipótesis, no es una optimización: es una corazonada.

## 3. Brief de onboarding (Fase 0)

```
NEGOCIO
- Producto/proyectos y ticket promedio: 
- Margen o comisión por venta: 
- Tasa de cierre lead calificado → venta: 
- Objetivo comercial del trimestre (unidades o ingresos): 
- CPL/CPA máximo tolerable (derivado, no deseado): 

EMBUDO
- CRM y quién lo administra: 
- SLA de primer contacto comprometido: 
- Quién marca las etapas y con qué frecuencia: 
- Criterio exacto de "lead calificado": 

TÉCNICO
- Accesos: Google Ads (admin), GA4, GTM, Merchant Center, CRM, dominio
- ¿El formulario guarda GCLID? ¿Hay Consent Mode? 
- Landings disponibles por intención: 

RESTRICCIONES
- Países de operación (¿EE.UU./Canadá? → política de vivienda)
- Marca: qué no se puede decir, qué precios se pueden publicar
- Competidores cuya marca NO se debe pujar
```

## 4. Ficha de experimento

```
Hipótesis: si ____________, entonces ____________ porque ____________
Tipo: [ ] Experimento de Google Ads  [ ] A/B de landing  [ ] A/B de asset set
Métrica primaria: ______  Métrica guardarraíl: ______
Duración mínima: 2 semanas o ___ conversiones
Resultado: ______  Decisión: [ ] adoptar  [ ] descartar  [ ] repetir
```

## 5. Checklist de auditoría rápida (30 min, cuenta nueva o heredada)

- [ ] Conversión primaria única, con valor, sin duplicados
- [ ] Enhanced conversions activas; consent mode si aplica
- [ ] Marca separada; exclusiones de marca en PMax
- [ ] Negativos a nivel cuenta cargados
- [ ] Ubicación configurada por "presencia"
- [ ] Landing por intención, formulario 3–5 campos, thank-you medida
- [ ] GCLID persistido en el CRM (>90% de los leads)
- [ ] Objetivos de puja alineados al rendimiento real de 30 días
- [ ] Campañas con <30 conversiones/mes: candidatas a consolidación
- [ ] Log de cambios existente y al día
