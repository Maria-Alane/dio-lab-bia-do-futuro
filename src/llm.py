import requests

def gerar_resposta(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.2
                }
            },
            timeout=300
        )

        response.raise_for_status()
        return response.json()["response"]

    except Exception as e:
        return f"Erro ao conectar com o modelo: {e}"