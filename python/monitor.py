import firebase_admin
from firebase_admin import credentials, db
import requests
import os
import json
from datetime import datetime

# 1. CONFIGURACIÓN DE SEGURIDAD (Híbrida)
# Este bloque detecta si el código corre en tu PC o en la nube
if 'FIREBASE_KEYS' in os.environ:
    # Caso: GitHub Actions (Usa el Secret que guardaste)
    firebase_info = json.loads(os.environ['FIREBASE_KEYS'])
    cred = credentials.Certificate(firebase_info)
else:
    # Caso: Local en tu Dell (Usa tu archivo JSON)
    cred = credentials.Certificate('serviceAccountKey.json')

# 2. INICIALIZAR FIREBASE
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://pagos-extreme-default-rtdb.firebaseio.com/'
    })

# 3. FUNCIÓN DE ENVÍO (Con tus tokens reales)
def enviar_telegram(mensaje):
    token = "8735212809:AAEN13dwh8AgjJXrWgy1NzjGBJU8eznKcbI" # @extreme_alertasbot
    chat_id = "8581959267" # ID de Cristina (Mama)
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': mensaje}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Error enviando mensaje: {e}")

# 4. LÓGICA DE REVISIÓN DE PAGOS
def revisar_pagos():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Revisando alumnos...")
    ref = db.reference('alumnos')
    alumnos = ref.get()
    
    if not alumnos:
        print("No hay alumnos registrados.")
        return

    for id, info in alumnos.items():
        nombre = info.get('nombre', 'Alumno desconocido')
        fecha_pago = info.get('fecha_pago') # Formato esperado: YYYY-MM-DD
        
        if fecha_pago:
            # Aquí puedes añadir tu lógica de días vencidos
            # Por ahora, enviamos una prueba si el campo existe
            enviar_telegram(f"✅ Sistema Activo: Revisando cuenta de {nombre}")
            print(f"Alerta procesada para: {nombre}")

if __name__ == "__main__":
    revisar_pagos()