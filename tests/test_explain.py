import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.parametrize(
    "payload, status_code",
    [
        ({"concept": "AI", "audience": "Kid"}, 200),
        ({"concept": "", "audience": "Kid"}, 422),  # updated
        ({"concept": "AI", "audience": ""}, 422),  # updated
        ({}, 422),
    ]
)
def test_explain(payload, status_code):
    """Test the explain endpoint with valid and invalid data."""
    response = client.post("/explain", json=payload)
    assert response.status_code == status_code
    if status_code == 200:
        data = response.json()
        assert "concept" in data
        assert "audience" in data
        assert "explanation" in data
