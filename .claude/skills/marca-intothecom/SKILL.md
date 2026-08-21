---
name: marca-intothecom
description: "Identidad visual y verbal de Intothecom (la agencia). Úsalo SIEMPRE que produzcas un entregable con la marca de la agencia: reportes mensuales, propuestas económicas, presentaciones, documentos, páginas, artifacts, plantillas o piezas internas. Define la paleta oficial (naranja #E86900, negro #1A1A1A, grises), la tipografía Be Vietnam Pro, los tokens CSS listos para usar y las reglas de contraste y aplicación. No aplica a piezas de clientes: esas usan la marca del cliente según su ficha."
---

# Marca Intothecom

**Intothecom · Agencia Marketing Digital.** Todo entregable con marca de la agencia usa esta identidad.
Si estás produciendo una pieza **para un cliente**, manda la marca del cliente (ver su ficha de marca):
esta identidad solo aparece en la firma o el pie.

## Regla que más se rompe

Los azules genéricos y las tipografías por defecto **no son de la marca**. Si estás por elegir un color
o una fuente para un documento de la agencia, la respuesta ya está aquí: no se inventa.

## Paleta

| Rol | HEX | RGB | Uso |
|---|---|---|---|
| Naranja de marca | `#E86900` | 232 · 105 · 0 | Acento, rellenos, barras, destaques, gráficos |
| Negro | `#1A1A1A` | 26 · 26 · 26 | Texto principal, fondos oscuros |
| Negro profundo | `#0F0F0F` | 15 · 15 · 15 | Fondos de portada y cortes de sección |
| Gris claro | `#E3E3E3` | 227 · 227 · 227 | Fondos de bloque, separadores |
| Blanco | `#FFFFFF` | 255 · 255 · 255 | Superficie base |
| Gris medio | `#777777` | 119 · 119 · 119 | Texto secundario, etiquetas |
| Gris borde | `#C9C9C9` | 201 · 201 · 201 | Líneas y bordes |
| Naranja tenue | `#FCEEDD` | 252 · 238 · 221 | Fondos de nota y destaque suave |
| Durazno | `#FFE7D2` | 255 · 231 · 210 | Fondos de alerta o segundo nivel |

**Contraste — la regla que evita entregables ilegibles:** `#E86900` sobre blanco no alcanza el contraste
mínimo para texto pequeño. Para **texto** en fondo claro se usa `#B85400`; el `#E86900` queda para
rellenos, barras, bordes, íconos y titulares grandes. En fondo oscuro, el acento de texto es `#FF8A2B`.

## Tipografía

**Be Vietnam Pro** para todo: títulos (600–700), texto (400–500), etiquetas (500 con letter-spacing).
Disponible en Google Fonts.

Para datos tabulares y códigos se admite una monoespaciada funcional (IBM Plex Mono) con
`font-variant-numeric: tabular-nums`. Nunca reemplaza a Be Vietnam Pro en texto de marca.

## Tokens listos para usar

Copiar tal cual en cualquier página, artifact o plantilla: `references/tokens.css`.
Incluye modo claro y oscuro, con el acento ajustado por contraste en cada uno.

## Reglas de aplicación

1. **Un solo acento.** El naranja se gana su lugar por escasez: si todo es naranja, nada destaca.
2. **Negro y grises hacen la estructura**; el naranja marca el dato que importa y la acción.
3. **Nunca gradientes de marca** ni combinaciones naranja sobre naranja tenue con texto pequeño.
4. **Jerarquía tipográfica clara**: un tamaño de título por nivel, no tres pesos en la misma línea.
5. **Firma**: "Intothecom | Agencia Marketing Digital" al pie de cada pieza, en gris medio.
6. **Datos siempre con tabular-nums** en tablas y KPIs: las cifras deben alinearse.
7. En gráficos, el naranja es la serie protagonista; el resto en escala de grises. Ver `references/aplicaciones.md`.

## Voz

Directa, concreta y sin relleno. La agencia habla de **resultados medibles**: cifra, período y comparación.
Nada de "sinergia", "soluciones integrales" ni superlativos sin dato. En reportes, el número del negocio
va primero; si el mes fue malo, se dice en la primera línea.
