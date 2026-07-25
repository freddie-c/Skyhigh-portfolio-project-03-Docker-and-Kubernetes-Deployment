from app import app


def test_count_increments():
    """The counter must strictly increase across calls.
    A smoke test proves /api/count responds; this proves it actually counts."""
    client = app.test_client()

    first = client.get("/api/count")
    second = client.get("/api/count")  # must return a higher number than the first.

    assert first.status_code == 200
    assert second.status_code == 200

    # Pull the count out of each JSON response and prove it went UP.
    first_count = first.get_json()["count"]
    second_count = second.get_json()["count"]
    assert second_count > first_count
