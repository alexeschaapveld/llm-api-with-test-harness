from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.ollama_client import generate_completion

app = FastAPI(title="Local LLM Gateway API");

#Defines the expected JSON structure
class GenerateRequest(BaseModel):
    prompt: str = Field(..., min_length=1, description="Prompt text to feed LLM")

#Defines the standard outgoing JSON structure
class GenerateResponse(BaseModel):
    response: str;

@app.get("/health")
async def health_check():
    """Simple health check endpoint for monitoring or readiness probing."""
    return {"status": "ok"}

@app.post("/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest):
    """Wrap Ollama generation logic into an HTTP POST route."""
    try:
        output_text = await generate_completion(request.prompt)
        return GenerateResponse(response=output_text)
    except Exception as e:
        #Security: Avoid exposing stack traces or sensitive information in production. Log the error internally and return a generic message.
        raise HTTPException(status_code=500, detail=f"LLM backend error: {str(e)}")