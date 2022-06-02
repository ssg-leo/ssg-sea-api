from fastapi.testclient import TestClient

test_text = "This course teaches the basic data manipulation skills using python and Excel for a data analytics career."


def test_api_status(client: TestClient) -> None:
    r = client.get("api/v1/health")
    assert r.status_code == 200
    health_message = r.json()
    assert health_message["message"] == "Welcome to the API"


def test_api_extraction(client: TestClient, test_text=test_text) -> None:
    payload = {
        "text": test_text
    }

    response = client.post(
        "http://localhost:8000/api/v1/extract",
        json=payload,
    )

    assert response.status_code == 200
    prediction_data = response.json()
    assert prediction_data["extractions"]
