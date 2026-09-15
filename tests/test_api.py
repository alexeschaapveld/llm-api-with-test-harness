#Checks that service is running under normal conditions
from fastapi.testclient import TestClient
from app.main import app

#Instatntiate an in-memory test client for FastAPI app.
client = TestClient(app)

def test_health_endpoint():
    """Verify that /health endpoint responds with HTTP 200 and standard status JSON."""
    #simulates incoming HTTP GET request to /health endpoint
    response = client.get("/health")

    #Test expectation against actual response
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
