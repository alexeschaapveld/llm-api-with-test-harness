import httpx
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint_healthy(monkeypatch):
    """Verify /health returns 200 with the correct body when Ollama is reachable."""
    class MockResponse:
        status_code = 200

    async def mock_get(self, url, **kwargs):
        return MockResponse()

    monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "ollama_status": "connected"}


def test_health_endpoint_ollama_unreachable(monkeypatch):
    """Verify /health returns 503 when Ollama can't be reached."""
    async def mock_get(self, url, **kwargs):
        raise httpx.ConnectError("connection refused")

    monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

    response = client.get("/health")
    assert response.status_code == 503
