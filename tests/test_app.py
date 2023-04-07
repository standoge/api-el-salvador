import pytest
from fastapi.testclient import TestClient

from app.internal.db import engine
from app.main import app

client = TestClient(app)


def test_db():
    """Test db connection"""
    try:
        engine.connect()
    except:
        assert False, "You're not connected to the database"


def test_department():
    """Test status code & get request for dep endpoint"""
    response = client.get("/departments/San Salvador")
    assert response.status_code == 200
    # here reponse.json() is a dict, so is needed specify by key
    assert response.json()["depname"] == "San Salvador"


def test_municipality():
    """Test status code & get request for mun endpoint"""
    response = client.get("/municipalities/Colon")
    assert response.status_code == 200
    # here reponse.json() is an array, so is needed specify by index as first element
    assert response.json()[0]["munname"] == "Colón"


def test_zone():
    """Test status code & get request for zone endpoint"""
    response = client.get("/zones/occidental")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_zipcodes():
    """Test status code & get request for zipcodes scraper endpoint"""
    response = client.get("/scraper/zipcodes/la_paz")
    assert response.status_code == 200
    assert response.json()["Zacatecoluca"] == "01601"


def test_image_bing():
    """Test status code & get request for images scraper endpoint"""
    response = client.get("/scraper/images/departments/usulutan")
    assert response.status_code == 200
    assert response.json() != [] or None
