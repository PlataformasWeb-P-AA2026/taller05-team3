### Actividades Realizadas

Se creó la carpeta **`formato-json`** para alojar los scripts de automatización encargados de la unificación y carga de datos. Se trabajó con los archivos proporcionados en la carpeta `data`:

*   **Fuente 1: `fuente_html_europa.html`** (Columnas: `nombre`, `seleccion`, `posicion`, `edad`, `club_actual`).
*   **Fuente 2: `fuente_csv_sudamerica.csv`** (Columnas: `nombre`, `seleccion`, `posicion`, `edad`, `partidos`).
*   **Fuente 3: `fuente_pdf_norteamerica_asia.pdf`** (Columnas: `Nombre`, `Seleccion`, `Posicion`, `Edad`, `Goles`).

#### Procesamiento y Unificación
Se utilizó el script `generar_json.py` para normalizar la información en un único archivo llamado **`mundial_2026.json`**. Este archivo se estructuró bajo la clave `{ "docs": [...] }` para cumplir con los requisitos de importación masiva de CouchDB.

#### Carga de Datos a la Base de Datos
Se desarrolló el script **`cargar_couch.py`**, el cual utiliza el endpoint **`_bulk_docs`** para automatizar la subida de los registros unificados directamente a la base de datos `jugadores` mediante peticiones HTTP.

> **Nota:** Esto se realizará después de haber creado la base de datos, lo cual se detalla en la actividad número 2.

#### Librerías de Python Utilizadas:
*   **`json`**: Para la manipulación y estructuración de los archivos de datos.
*   **`csv`**: Para la lectura de la fuente de Sudamérica.
*   **`pypdf` (PdfReader)**: Para la extracción de texto del archivo PDF.
*   **`bs4` (BeautifulSoup)**: Para el parseo de la tabla HTML de Europa.
*   **`requests`**: Para gestionar la comunicación con la API de CouchDB y realizar la carga masiva.
