from app import app


def test_health_returns_200():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200


def test_index_renders_when_backend_unreachable():
    # Frontend degrades gracefully when the backend is down
    # (Fix for README Challenge #2). No backend exists on the CI runner, so
    # this asserts that documented behavior: a rendered page, not a 500.
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200