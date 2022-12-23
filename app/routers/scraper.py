import os

from fastapi import APIRouter
from zipcode.department import Department, Endpoint

from serpapi import GoogleSearch

router = APIRouter()

G_KEY = os.environ["G_KEY"]


@router.get(path="/scraper/zipcodes/{dep_name}", tags=["SCRAPER"])
def get_zipcodes(dep_name: str):
    """Return municipalities by department and their zip codes in json format."""
    departament_zipcode = Department(Endpoint[f"{dep_name}"].value)
    return departament_zipcode.zip_codes


@router.get(path="/scraper/images/{dep_name}", tags=["SCRAPER"])
def get_images(dep_name: str):
    """Return images url with metadata from Google by department."""
    params = {
        "q": f"El Salvador {dep_name}",
        "tbm": "isch",
        "ijin": 0,
        "api_key": G_KEY,
    }

    search = GoogleSearch(params)

    results = search.get_dict()["images_results"]
    return results
