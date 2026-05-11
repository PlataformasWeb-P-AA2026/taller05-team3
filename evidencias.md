### Actividades Realizadas

Se creó la carpeta **`formato-json`** para alojar los scripts de automatización encargados de la unificación y carga de datos. Se trabajó con los archivos proporcionados en la carpeta `data`:

*   **Fuente 1: `fuente_html_europa.html`** (Columnas: `nombre`, `seleccion`, `posicion`, `edad`, `club_actual`).
*   **Fuente 2: `fuente_csv_sudamerica.csv`** (Columnas: `nombre`, `seleccion`, `posicion`, `edad`, `partidos`).
*   **Fuente 3: `fuente_pdf_norteamerica_asia.pdf`** (Columnas: `Nombre`, `Seleccion`, `Posicion`, `Edad`, `Goles`).
## Evidencias  carpeta 

<img width="896" height="285" alt="image" src="https://github.com/user-attachments/assets/f77e44aa-2a1e-465e-a2c0-c01b67033052" />

#### Procesamiento y Unificación
Se utilizó el script `generar_json.py` para normalizar la información en un único archivo llamado **`mundial_2026.json`**. Este archivo se estructuró bajo la clave `{ "docs": [...] }` para cumplir con los requisitos de importación masiva de CouchDB. (se uso `python generar_json.py` para ejecutar el script )

## Evidencias  mundial_2026.json

<img width="1018" height="375" alt="image" src="https://github.com/user-attachments/assets/e66bcae8-4ab5-462e-a25d-52f01e063d8b" />

<img width="592" height="772" alt="image" src="https://github.com/user-attachments/assets/62d18234-80a0-4556-a2b4-4e39859d06a0" />


#### Carga de Datos a la Base de Datos
Se desarrolló el script **`cargar_couch.py`**, el cual utiliza el endpoint **`_bulk_docs`** para automatizar la subida de los registros unificados directamente a la base de datos `jugadores` mediante peticiones HTTP.

## Evidencias  cargar_couch.py



> **Nota:** Esto se realizará después de haber creado la base de datos, lo cual se detalla en la actividad número 2.

#### Librerías de Python Utilizadas:
*   **`json`**: Para la manipulación y estructuración de los archivos de datos.
*   **`csv`**: Para la lectura de la fuente de Sudamérica.
*   **`lxml`**: Funciona como motor de parseo de alto rendimiento para procesar estructuras XML y HTML complejas de forma rápida. (pip install lxml).
*   **`pypdf` (PdfReader)**: Para la extracción de texto del archivo PDF. (pip install pypdf)
*   **`bs4` (BeautifulSoup)**: Para el parseo de la tabla HTML de Europa. (pip install beautifulsoup4)
*   **`requests`**: Para gestionar la comunicación con la API de CouchDB y realizar la carga masiva. (pip install requests)

## Evidencias  librerias 

<img width="1902" height="743" alt="image" src="https://github.com/user-attachments/assets/7adb00eb-b5bb-4a42-aa88-99726cd9820c" />




