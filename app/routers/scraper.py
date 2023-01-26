import os

from fastapi import APIRouter, Query
from souvenir.image import ImageAzure, ImageBing, ImageGoogle
from souvenir.zipcode import Endpoint, Zipcode

router = APIRouter()

G_KEY = os.environ["G_KEY"]
A_KEY = os.environ["A_KEY"]
ENDPOINT = os.environ["ENDPOINT"]


@router.get(path="/scraper/zipcodes/{dep_name}", tags=["SCRAPER"])
def get_zipcodes(dep_name: str):
    """Return municipalities by department and their zip codes in json format.

    **Args:**\t
        `dep_name:` Name of department to search zipcodes.\t
        Incluides zipcodes for all municipalities within the searched department.


    """
    departament_zipcode = Zipcode(Endpoint[f"{dep_name}"].value)
    return departament_zipcode.codes


@router.get(path="/scraper/images/departments/{dep_name}", tags=["SCRAPER"])
def get_img_dep(dep_name: str, engine: str = Query(default=None)):
    """Return images url with metadata from Bing or Google engine by department.

    **Args:**\t
         `dep_name:`Name of department to search images about.\t
         `engine:`Defaults to Bing. To use Google or official Bing engine you will need an API_KEY.

    """
    if engine is not None:

        # act like a switch case
        engines = {
            "google": ImageGoogle(f"{dep_name} departamento", G_KEY).images,
            "bing": ImageAzure(f"{dep_name} departamento", A_KEY, ENDPOINT).images,
        }

        results = engines.get(engine, "Invalid engine")
        return results

    results = ImageBing(f"{dep_name} departamento").images
    return results


@router.get(path="/scraper/images/municipalities/{mun_name}", tags=["SCRAPER"])
def get_img_mun(mun_name: str, engine: str = Query(default=None)):
    """Return images url with metadata from Bing or Google engine by municipality.

    **Args:**\t
         `mun_name:`Name of municipality to search images about.\t
         `engine:`Defaults to Bing. To use Google or official Bing engine you will need an API_KEY.

    """
    if engine is not None:

        # act like a switch case
        engines = {
            "google": ImageGoogle(f"{mun_name} municipio", G_KEY).images,
            "bing": ImageAzure(f"{mun_name} municipio", A_KEY, ENDPOINT).images,
        }

        results = engines.get(engine, "Invalid engine")
        return results

    results = ImageBing(f"{mun_name} municipio").images
    return results
