from app.app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "SecureApp"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"


def test_info():
    client = app.test_client()

    response = client.get("/info")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "secureapp"
    assert data["version"] == "1.0.0"