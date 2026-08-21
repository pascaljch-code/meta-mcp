# Nomenclatura y UTMs

Sin convención, a los tres meses nadie puede responder "¿qué ángulo rindió mejor este trimestre?".
La nomenclatura no es orden estético: es lo que hace posible el análisis agregado.

## Estructura

**Campaña**
```
[PLATAFORMA]_[CLIENTE]_[OBJETIVO]_[ETAPA]_[GEO]_[MES]
GA_NEV_LEADS_CAPTURA_STGO_2026-09
MT_NEV_LEADS_PROSPECTING_STGO_2026-09
```

**Conjunto / grupo de anuncios**
```
[SEGMENTO O INTENCIÓN]_[DETALLE]
DEPTOS-NUNOA_AMPLIO
CREDITO-HIPOTECARIO_EXACTA
```

**Anuncio**
```
[ANGULO]_[FORMATO]_[HOOK O VARIANTE]_[VERSION]
PRECIO-DESDE_VID916_HOOKA_v1
AVANCE-OBRA_CARR_TARJETA-PROCESO_v2
```

Reglas: siempre mayúsculas y guiones; nunca espacios ni acentos; el **ángulo va primero** en el anuncio,
porque es la variable que más se analiza; la versión se incrementa cuando cambia la pieza, no cuando
cambia el título.

## UTMs

```
utm_source=google | facebook
utm_medium=cpc | paid_social
utm_campaign={nombre de campaña}
utm_content={angulo}-{formato}-{hook}
utm_term={keyword} (solo Search)
```

Usar los parámetros dinámicos de cada plataforma para no escribirlos a mano, y verificar que la landing
los conserve tras cualquier redirección. Una redirección que borra los UTMs deja el análisis ciego y nadie
se entera hasta el cierre de mes.

## Registro paralelo

La nomenclatura vive en la plataforma; el **registro de ángulos** vive en la ficha de marca. Ambos deben
coincidir: el nombre del anuncio y el ángulo del registro se escriben igual, o el cruce no se puede hacer.
