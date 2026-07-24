# Smoke test for the backend's /health endpoint — the same endpoint the Kubernetes 
# readiness and liveness probes hit. If this fails, the pod would never reach 1/1 READY 
# so it's the right CI gate.

from app import app  # resolves because conftest.py puts backend/ on sys.path


def test_health_returns_200():
    # test_client() calls Flask routes IN-PROCESS — no server starts, no socket binds, 
    # port 5001 is irrelevant. Runs in milliseconds.
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200


def test_api_count_returns_200():
    # The actual API endpoint. Guards against a broken route slipping through 
    # just because /health still answers.
    client = app.test_client()
    response = client.get("/api/count")
    assert response.status_code == 200