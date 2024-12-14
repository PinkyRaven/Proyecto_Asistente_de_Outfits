
from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt
import pandas as pd
import io
import base64
import requests

app = Flask(__name__)

# Ruta de la página principal
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para procesar las selecciones del usuario y generar un prompt para DALL·E
@app.route('/generate_outfit', methods=['POST'])
def generate_outfit():
    data = request.json  # Recibimos las prendas seleccionadas
    selected_items = data.get('selected_items', [])
    
    # Generar el prompt en base a las prendas seleccionadas
    if not selected_items:
        return jsonify({"error": "No se seleccionaron prendas."}), 400
    
    prompt = "Un outfit con las siguientes prendas: " + ", ".join(selected_items)
    
    # Llamar a la API de OpenAI (requiere configurar tu API Key)
    api_key = "TU_API_KEY"  # Reemplaza con tu API Key de OpenAI
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    dall_e_payload = {
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }
    
    try:
        response = requests.post("https://api.openai.com/v1/images/generations", headers=headers, json=dall_e_payload)
        response_data = response.json()
        image_url = response_data['data'][0]['url']
        return jsonify({"image_url": image_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ruta para mostrar un gráfico de prendas seleccionadas
@app.route('/stats')
def stats():
    # Datos ficticios de ejemplo (puedes conectar esto a tu base de datos)
    data = {
        'Prenda': ['Camiseta', 'Pantalón', 'Chaqueta'],
        'Veces Seleccionada': [5, 3, 2]
    }
    df = pd.DataFrame(data)
    
    # Crear el gráfico
    plt.figure(figsize=(8, 6))
    df.plot(kind='bar', x='Prenda', y='Veces Seleccionada', color='skyblue', legend=False)
    plt.title("Prendas Seleccionadas")
    plt.xlabel("Prenda")
    plt.ylabel("Veces Seleccionada")
    
    # Guardar gráfico en un objeto BytesIO
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
    
    return render_template('stats.html', img_str=img_base64)

if __name__ == '__main__':
    app.run(debug=True)
