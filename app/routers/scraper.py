import os

from fastapi import APIRouter, Query
from souvenir.zipcode import Endpoint, Zipcode
from souvenir.image import ImageBing, ImageGoogle


router = APIRouter()

G_KEY = os.environ["G_KEY"]


@router.get(path="/scraper/zipcodes/{dep_name}", tags=["SCRAPER"])
def get_zipcodes(dep_name: str):
    """Return municipalities by department and their zip codes in json format.

    `Args:`\t
        **dep_name:** Name of department to search zipcodes.\t
        Incluides zipcodes for all municipalities within the searched department.


    """
    departament_zipcode = Zipcode(Endpoint[f"{dep_name}"].value)
    return departament_zipcode.zip_codes


@router.get(path="/scraper/images/{dep_name}", tags=["SCRAPER"])
def get_images(dep_name: str, engine: str = Query(default=None)):
    """Return images url with metadata from Bing or Google engine by department.

    `Args:`\t
         **dep_name:** Name of department to search images about.\t
         **engine:** Defaults to Bing. To use Google engine you will need an API_KEY.

    """
    if engine is not None:
        results = ImageGoogle(dep_name, G_KEY).images
        return results
    results = ImageBing(dep_name).images
    return results
