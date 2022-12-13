from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "From FastAPI"}


def test_departament():
    """Test status code & get request for dep endpoint"""
    response = client.get("/departaments/San Salvador")
    assert response.status_code == 200
    assert response.json()["depname"] == "San Salvador"


def test_municipality():
    """Test status code & get request for mun endpoint"""
    response = client.get("/municipalities/Colon")
    assert response.status_code == 200
    # here reponse.json() is an array, so is needed specify by index as first element
    assert response.json()[0]["munname"] == "Colón"
