### 1. Actividades Realizadas
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

### Actividad 2: Creación de Base de Datos y Vistas en CouchDB

En esta fase se procedió con la configuración del entorno en CouchDB para la persistencia y consulta de los datos unificados.

#### 1. Creación de la Base de Datos
Se creó una nueva base de datos denominada **`jugadores`**. Esta base de datos alojará los documentos generados por el script de unificación.

* **Evidencia:**

  <img width="1918" height="607" alt="image" src="https://github.com/user-attachments/assets/57ee61c6-ad4d-4e9b-b863-46f58a157523" />

#### 2. Configuración de Design Document y Vistas (Map Functions)
Para optimizar las consultas y organizar la información según los campos específicos de cada región, se creó un Design Document llamado **`_design/losjugadores`**. Dentro de este, se implementaron tres vistas dinámicas:

* **Vista `por_club`**: Filtra y organiza a los jugadores según su club actual (campo proveniente de la fuente europea).
    ```javascript
    function(doc) {
      if (doc.club_actual) {
        emit(doc.club_actual, doc);
      }
    }
    ```
    * **Evidencia:** *

      <img width="536" height="651" alt="image" src="https://github.com/user-attachments/assets/aceb62c9-5b27-45d4-b5a7-cb70db0fe7f5" />

* **Vista `por_goles`**: Indexa a los jugadores en función de su cantidad de goles marcados (campo proveniente de la fuente de Norteamérica y Asia).
    ```javascript
    function(doc) {
      if (doc.goles) {
        emit(doc.goles, doc);
      }
    }
    ```
    * **Evidencia:**
      
      <img width="521" height="692" alt="image" src="https://github.com/user-attachments/assets/e6302a51-93f3-4937-9328-97d8c121db48" />

* **Vista `por_partidos`**: Organiza los registros basados en el número de partidos disputados (campo proveniente de la fuente sudamericana).
    ```javascript
    function(doc) {
      if (doc.partidos) {
        emit(doc.partidos, doc);
      }
    }
    ```
    * **Evidencia:**
      
      <img width="518" height="657" alt="image" src="https://github.com/user-attachments/assets/12130b04-2556-4a60-a20e-5f3a44ebd86d" />

#### 3. Verificación de Documentos Cargados
Una vez ejecutado el script de carga masiva, se verificó en el panel de control de CouchDB (Fauxton) que los documentos se encuentran correctamente indexados y accesibles a través de las vistas creadas.

* **Evidencia:** *(Aquí debes insertar la captura `image_89a876.png` que muestra el listado de documentos ya cargados en la base de datos)*

















