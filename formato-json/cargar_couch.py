import requests
import json

# Configuración de tu CouchDB
URL = "http://admin:admin@127.0.0.1:5985/jugadores" 
ARCHIVO = "mundial_2026.json"

try:
    
    with open(ARCHIVO, 'r', encoding='utf-8') as f:
        datos = json.load(f)
    
    
    # Usamos _bulk_docs para cargar todo de un solo golpe
    response = requests.post(f"{URL}/_bulk_docs", json=datos)

    # 3. Verificar si la carga fue exitosa (Código 201 es 'Created')
    if response.status_code == 201:
        print("¡Éxito! Los registros se cargaron en la base de datos 'jugadores'.")
    else:
        print(f"Error al cargar: {response.text}")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")