from fastapi import APIRouter, Depends
from zipcode.departments import Departments, Endpoint

router = APIRouter()


@router.get(path="/scrapper/{dep_name}", tags=["SCRAPPER"])
def get_zipcodes(dep_name: str):
    """Returns departaments data in json format."""
    departament = Departments(Endpoint.dep_name.value)
    return department.zip_codes
