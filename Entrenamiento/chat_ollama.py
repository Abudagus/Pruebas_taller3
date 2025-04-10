import requests

def enviar_prompt(pregunta):
    prompt = f"""Eres un asistente experto. Responde con claridad.
    
    Pregunta: {pregunta}
    Respuesta:"""

    respuesta = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': 'llama3:8b',
            'prompt': prompt,
            'stream': False
        }
    )

    return respuesta.json()['response'].strip()


if __name__ == "__main__":
    pregunta = input("Tu pregunta: ")
    print("Respuesta:", enviar_prompt(pregunta))
