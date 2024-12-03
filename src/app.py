from flask import Flask, request, render_template, jsonify
import openai

app = Flask(__name__)

# Configura tu clave de API
openai.api_key = "TU_API_KEY"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_choices = request.json.get('choices')  # Selecciones del usuario
    prompt = f"Genera un outfit basado en estas elecciones: {', '.join(user_choices)}"
    
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return jsonify({'image_url': image_url})

if __name__ == '__main__':
    app.run(debug=True)
