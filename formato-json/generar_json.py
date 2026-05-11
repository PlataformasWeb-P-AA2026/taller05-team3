import json
import csv
from pypdf import PdfReader
from bs4 import BeautifulSoup

# 1. Rutas
ruta_csv = "../data/fuente_csv_sudamerica.csv"
ruta_html = "../data/fuente_html_europa.html"
ruta_pdf = "../data/fuente_pdf_norteamerica_asia.pdf"

lista_final = []

# --- PARTE A: CSV (Sudamerica) ---

with open(ruta_csv, encoding='utf-8') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        lista_final.append({
            "nombre":    fila["nombre"],
            "seleccion": fila["seleccion"],
            "posicion":  fila["posicion"],
            "edad":      int(fila["edad"]),
            "partidos":  int(fila["partidos"])
        })

# --- PARTE B: HTML (Europa) ---
# Esta fuente trae 'club_actual' pero NO trae 'goles' ni 'partidos'.
with open(ruta_html, encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')
    filas_html = soup.find_all('tr')
    for tr in filas_html[1:]:  # Saltamos el encabezado <th>
        celdas = tr.find_all('td')
        if len(celdas) >= 5:
            lista_final.append({
                "nombre":      celdas[0].text.strip(),
                "seleccion":   celdas[1].text.strip(),
                "posicion":    celdas[2].text.strip(),
                "edad":        int(celdas[3].text.strip()) if celdas[3].text.strip().isdigit() else 0,
                "club_actual": celdas[4].text.strip()
            })

# --- PARTE C: PDF (Norteamérica y Asia) ---

ENCABEZADOS_PDF = {"Nombre", "Seleccion", "Posicion", "Edad", "Goles"}

tokens = []
lector_pdf = PdfReader(ruta_pdf)
for pagina in lector_pdf.pages:
    texto = pagina.extract_text() or ""
    # split() sin argumento divide por cualquier whitespace
    # (espacios, tabs, saltos de línea).
    for parte in texto.split():
        if parte not in ENCABEZADOS_PDF:
            tokens.append(parte)

# Agrupamos de 5 en 5: nombre, seleccion, posicion, edad, goles
i = 0
while i + 4 < len(tokens):
    nombre, seleccion, posicion, edad, goles = tokens[i:i + 5]
    if edad.isdigit() and goles.isdigit():
        lista_final.append({
            "nombre":    nombre,
            "seleccion": seleccion,
            "posicion":  posicion,
            "edad":      int(edad),
            "goles":     int(goles)
        })
        i += 5
    else:
        #   Avanzamos 1 y seguimos.(omitir encabesado)
        i += 1

# 2. Formato final para CouchDB
resultado_couch = {
    "docs": lista_final
}

# 3. Guardar
with open("mundial_2026.json", "w", encoding='utf-8') as j:
    json.dump(resultado_couch, j, indent=4, ensure_ascii=False)

print(f"¡Éxito! Procesados {len(lista_final)} registros unificados.")