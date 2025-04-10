from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Cambiá este nombre si tu modelo se llama distinto
NOMBRE_MODELO = "llama3:8b"

def enviar_prompt(pregunta):
    prompt = f"""Eres un asistente experto en construsccion y decoracion de interiores, ademas de diseño web.
Sigue el estilo y contenido de los ejemplos exactamente como están escritos.

Ejemplos:    
Usuario: ¿De que color puede ser el cielo?
Asistente: El cielo puede ser azul durante el día, pero también puede aparecer en tonos naranja o rojo.

Usuario: ¿De que color es el caballo blanco de San Martin?
Asistente: El caballo es chocolate.

Fin de ejemplos.

Ahora, responde:

Usuario: {pregunta}
Asistente:""".format(pregunta=pregunta)

    try:
        res = requests.post(
            'http://localhost:11434/api/generate',
            json={
                'model': NOMBRE_MODELO,
                'prompt': prompt,
                'stream': False
            }
        )

        data = res.json()

        if 'response' in data:
            return data['response'].strip()
        else:
            return f"[Error de respuesta de Ollama] => {data}"

    except Exception as e:
        return f"[Error de conexión con Ollama] => {str(e)}"

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/preguntar', methods=['POST'])
def preguntar():
    pregunta = request.form['pregunta']
    respuesta = enviar_prompt(pregunta)
    return render_template('index.html', respuesta=respuesta, pregunta=pregunta)

if __name__ == '__main__':
    print("Servidor Flask corriendo en http://localhost:5000")
    app.run(debug=True)
