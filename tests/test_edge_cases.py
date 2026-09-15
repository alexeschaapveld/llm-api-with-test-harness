#Checks how service responds to bad or malicious inputs
#Referred to as negative testing

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_empty_prompt_rejected():
    """Verify that empty string triggers a Pydantic validation error. """
    payload = {"prompt": ""}
    response = client.post("/generate", json=payload)

    #FastAPI should return an 422 Unprocessable Entity status code for validation errors"""
    assert response.status_code == 422

def test_invalid_json_payload():
    """Malformed non-JSON content types should be rejected by FastAPI."""
    response = client.post(
        "/generate", 
        content="not valid json", 
        headers={"Content-Type": "application/json"}  # Added opening quote here
    )
    
    assert response.status_code == 422