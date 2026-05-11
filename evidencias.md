### Actividades Realizadas

Se creó la carpeta **`formato-json`** para colocar el script de Python que se usará para unificar los datos de los diferentes archivos proporcionados de la carpeta `data`:

*   **Fuente 1: `fuente_html_europa.html`**
    *   Columnas encontradas: `nombre`, `seleccion`, `posicion`, `edad` y `club_actual`.
*   **Fuente 2: `fuente_csv_sudamerica.csv`**
    *   Columnas encontradas: `nombre`, `seleccion`, `posicion`, `edad` y `partidos`.
*   **Fuente 3: `fuente_pdf_norteamerica_asia.pdf`**
    *   Columnas encontradas: `Nombre`, `Seleccion`, `Posicion`, `Edad` y `Goles`.

Para este proceso se utilizaron las siguientes librerías de Python:

*   **`json`**: Para generar el archivo final con formato de datos estructurados.
*   **`csv`**: Para procesar los datos provenientes de la fuente de Sudamérica.
*   **`pypdf` (PdfReader)**: Para realizar la extracción de texto de la fuente de Norteamérica y Asia.
*   **`bs4` (BeautifulSoup)**: Para aplicar técnicas de web scraping sobre la fuente de Europa.

Todo se unificó en un archivo llamado **`mundial_2026.json`**, el cual cuenta con la estructura requerida por **CouchDB**: `{ "docs": [ { ... }, { ... } ] }`, permitiendo así su importación masiva directa a la base de datos.
