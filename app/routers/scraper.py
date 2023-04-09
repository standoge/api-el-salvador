import os

from fastapi import APIRouter
from souvenir.image import ImageBing
from souvenir.zipcode import Endpoint, Zipcode

from app.internal.schemas import Zipzip

router = APIRouter()

A_KEY = os.environ["A_KEY"]
ENDPOINT = os.environ["ENDPOINT"]


@router.get(
    path="/scraper/zipcodes/{dep_name}",
    tags=["SCRAPER"],
    responses={200: {"model": Zipzip}},
)
def get_zipcodes(dep_name: str):
    """Return municipalities by department and their zip codes in json format.

    **Args:**\t
        `dep_name:` Name of department to search zipcodes.\t
        Incluides zipcodes for all municipalities within the searched department.
    """
    departament_zipcode = Zipcode(Endpoint[f"{dep_name}"].value)
    return departament_zipcode.codes


@router.get(path="/scraper/images/departments/{dep_name}", tags=["SCRAPER"])
def get_img_dep(dep_name: str):
    """Return images url with metadata from Bing engine by department.

    **Args:**\t
         `dep_name:`Name of department to search images about.\t
    """
    results = ImageBing(f"{dep_name} departamento", A_KEY, ENDPOINT).images
    return results


@router.get(path="/scraper/images/municipalities/{mun_name}", tags=["SCRAPER"])
def get_img_mun(mun_name: str):
    """Return images url with metadata from Bing engine by municipality.

    **Args:**\t
         `mun_name:`Name of municipality to search images about.\t
    """
    results = ImageBing(f"{mun_name} municipio", A_KEY, ENDPOINT).images
    return results
