import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate(prompt):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "tinyllama-rag",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    return data["response"]