from fastapi import APIRouter
from zipcode.department import Department, Endpoint

router = APIRouter()


@router.get(path="/scraper/{dep_name}", tags=["SCRAPER"])
def get_zipcodes(dep_name: str):
    """Returns departaments data in json format."""
    departament_zipcode = Department(Endpoint[f"{dep_name}"].value)
    return departament_zipcode.zip_codes
