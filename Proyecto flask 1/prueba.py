import requests

url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}

data = {
    "model": "llama3:8b",  # Este es el nombre del modelo
    "prompt": "Contame sobre la nintento switch",
    "stream": False     # Si lo ponés en True, te devuelve respuesta en partes
}

response = requests.post(url, headers=headers, json=data)

# Mostrar la respuesta
# print(response.json())
respuesta = response.json()["response"]
print(respuesta)