from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "From FastAPI"}


def test_department():
    """Test status code & get request for dep endpoint"""
    response = client.get("/departments/San Salvador")
    assert response.status_code == 200
    assert response.json()["depname"] == "San Salvador"


def test_municipality():
    """Test status code & get request for mun endpoint"""
    response = client.get("/municipalities/Colon")
    assert response.status_code == 200
    # here reponse.json() is an array, so is needed specify by index as first element
    assert response.json()[0]["munname"] == "Colón"


def test_zipcodes():
    """Test status code & get request for zipcodes scraper endpoint"""
    response = client.get("/scraper/zipcodes/la_paz")
    assert response.status_code == 200
    # here reponse.json() is a dict, so is needed specify by key
    assert response.json()["Zacatecoluca"] == "01601"


def test_images():
    """Test status code & get request for images scraper endpoint"""
    response = client.get("/scraper/images/usulutan")
    assert response.status_code == 200
