import httpx

OLLAMA_URL = "http://localhost:11434/api/generate"

#Local AI model can be changed HERE
async def generate_completion(prompt: str, model: str = "smolLm2:135M") -> str:
    """Sends prompt to local Ollama instance and returns generated response"""
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False #Easier for load testing and debugging
    }

    #30 sec timeout
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        data=response.json()
        return data.get("response", "")