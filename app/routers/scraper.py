import os
from functools import wraps

from fastapi import APIRouter, Query
from souvenir.zipcode import Endpoint, Zipcode
from souvenir.image import ImageBing, ImageGoogle


router = APIRouter()

G_KEY = os.environ["G_KEY"]


def key_error(operation):
    """Handle KeyError exception for values that aren't in Endpoint enum."""

    @wraps(operation)
    def wrapper(**kwargs):
        try:
            return operation(**kwargs)
        except KeyError:
            return {"error": "department not found"}

    return wrapper


@router.get(path="/scraper/zipcodes/{dep_name}", tags=["SCRAPER"])
@key_error
def get_zipcodes(dep_name: str):
    """Return municipalities by department and their zip codes in json format."""
    departament_zipcode = Zipcode(Endpoint[f"{dep_name}"].value)
    return departament_zipcode.zip_codes


@router.get(path="/scraper/images/{dep_name}", tags=["SCRAPER"])
@key_error
def get_images(dep_name: str):
    """Return images url with metadata from Bing by department."""
    results = ImageBing(dep_name).images
    return results


@router.get(path="/scraper/images/{dep_name}", tags=["SCRAPER"])
@key_error
def get_images(dep_name: str, engine: str = Query(default=None)):
    """Return images url with metadata from Bing by department."""
    if engine != "google":
        {"error": "engine not found"}
    results = ImageGoogle(dep_name, G_KEY).images
    return results
