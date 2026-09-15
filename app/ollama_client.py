import httpx
from fastapi import HTTPException, status

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "smollm2:135m"

async def generate_completion(prompt: str) -> str:
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                OLLAMA_URL,
                json={"model": MODEL_NAME, "prompt": prompt, "stream": False}
            )
            response.raise_for_status()
            data = response.json()
            return data.get("response", "")
            
    except httpx.TimeoutException:
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail="Request timed out while waiting for local LLM inference"
        )
    except httpx.ConnectError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Failed to connect to local Ollama service"
        )
    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ollama returned an error: {exc.response.text}"
        )