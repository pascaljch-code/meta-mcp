# Contexto — Propuesta Dale Coopeuch

Si estás trabajando en esta carpeta, **lee `ESTADO.md` completo antes de hacer nada**.
Contiene las decisiones ya cerradas, las correcciones pendientes y un bloqueante sin
resolver.

## Lo mínimo que no puedes ignorar

- **Precios: sin descuentos por paquete.** Paid Media 35 UF, Community Management 25 UF,
  Email Marketing 25 UF, todos + IVA 19%. Datapify USD 299 + IVA, contratado directo por
  el cliente y expresado en dólares. No los cambies ni los recalcules sin instrucción.
- **No inventes información sensible.** Todo dato lleva fuente y fecha. Lo que no se puede
  respaldar se declara como pendiente. Nunca se rellena con estimaciones.
- **No rediseñes.** Se replica la línea gráfica de las propuestas base de Intothecom:
  Be Vietnam Pro, naranjo `#E57000`, formato 10 × 5,625 pulgadas. Los helpers están en
  `generadores/deck_lib.py` y `generadores/slides.py`.
- **Bloqueante abierto:** puede que Google Search esté cerrado para crédito de consumo en
  Chile por el requisito de divulgación. Sección 3 de `ESTADO.md`. No presentar la
  propuesta afirmando que Search es viable hasta resolverlo.
- **Monteclaro no se menciona** en ningún documento. Es contexto interno.
- **Sin grabación de contenidos.** No es un servicio de esta propuesta.

## Cómo regenerar los documentos

```bash
pip install python-pptx python-docx openpyxl pymupdf pillow
# Fuente Be Vietnam Pro desde github.com/google/fonts/tree/main/ofl/bevietnampro → ~/.fonts
cd generadores
python3 build_propuesta.py   # 01 PPTX
python3 build_xlsx.py        # 02 XLSX
python3 build_docx.py        # 03 DOCX
python3 build_resumen.py     # 04 PPTX resumen
```

Para verificar visualmente hay que convertir a PDF y renderizar las páginas. Requiere
`libreoffice-impress`, `libreoffice-calc` y `libreoffice-writer`. El navegador headless
está bloqueado por el proxy del entorno remoto: no sirve para verificar sitios externos.
