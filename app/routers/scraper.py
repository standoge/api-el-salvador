import os

from fastapi import APIRouter, Query
from souvenir.zipcode import Endpoint, Zipcode
from souvenir.image import ImageBing, ImageGoogle


router = APIRouter()

G_KEY = os.environ["G_KEY"]


@router.get(path="/scraper/zipcodes/{dep_name}", tags=["SCRAPER"])
def get_zipcodes(dep_name: str):
    """Return municipalities by department and their zip codes in json format."""
    departament_zipcode = Zipcode(Endpoint[f"{dep_name}"].value)
    return departament_zipcode.zip_codes


@router.get(path="/scraper/images/{dep_name}", tags=["SCRAPER"])
def get_images(dep_name: str, engine: str = Query(default=None)):
    """Return images url with metadata from Bing or Google engine by department."""
    if engine is not None:
        results = ImageGoogle(dep_name, G_KEY).images
        return results
    results = ImageBing(dep_name).images
    return results
