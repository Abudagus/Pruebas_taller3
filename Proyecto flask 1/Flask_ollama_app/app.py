from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

OLLAMA_API_URL = "http://localhost:11434/api/generate"  # URL de la API de Ollama
MODEL_NAME = "llama3:8b"  # Nombre del modelo de Ollama

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preguntar', methods=['POST'])
def preguntar():
    pregunta = request.json.get('pregunta')
    if not pregunta:
        return jsonify({"error": "No se envió una pregunta"}), 400

    try:
        respuesta =requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3:8b",  
                "prompt": pregunta,
                "stream": False  # Cambia a True si quieres respuesta en partes
            },
        )
        data = respuesta.json()
        return jsonify({'respuesta': data['response']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Iniciando el servidor Flask...")
    app.run(debug=True, port=5000)  # Cambia el puerto si es necesario
# Iniciar el servidor Flask con el comando: python app.py