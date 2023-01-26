"""Postgresql is case sensitive, so we need to use ilike"""
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import ReturnTypeFromArgs

import app.internal.models as models


class unaccent(ReturnTypeFromArgs):
    """Unaccent function for postgresql"""


def query_encoder(request):
    """Transform sqlalchemy object returned by query to json"""

    def wrapper(*args):
        """Besides check if reponse isn't None or []"""
        query_result = request(*args)
        if query_result is None or query_result == []:
            return JSONResponse(
                content={"query encoder error": "That value doesn't exists"},
                status_code=500,
            )
        return JSONResponse(status_code=200, content=jsonable_encoder(query_result))

    return wrapper


@query_encoder
def get_department(db: Session, dp_name: str):
    """Return the first match with dp_name argument in depsv table."""
    # fmt: off
    query_response = (
        db.query(models.Department)
        .filter(
            unaccent(models.Department.depname).ilike(f"{dp_name}")
        )
        .first()
    )

    return query_response


@query_encoder
def get_municipality(db: Session, mun_name: str):
    """Return the first match with mun_name argument in munsv table."""
    # fmt: off
    query_response = (
        db.query(models.Municipality)
        .filter(
            unaccent(models.Municipality.munname).ilike(f"{mun_name}%")
        )
        .all()
    )

    return query_response


@query_encoder
def get_municipality_by_dep(db: Session, mun_name: str, dep_name: str):
    """Return the first match with mun_name in munsv table."""
    # fmt: off
    query_response = (
        db.query(models.Municipality)
        .filter(
            unaccent(models.Municipality.munname).ilike(f"{mun_name}%"),
            unaccent(models.Municipality.department).has(
                unaccent(models.Department.depname) == dep_name
            )
        )
        .first()
    )

    return query_response


@query_encoder
def get_zone(db: Session, zone_name: str):
    """Return the first match with zone_name argument in zonesv table."""
    # fmt: off
    query_response = (
        db.query(models.Zone)
        .filter(
            models.Zone.zonename.ilike(f"{zone_name}")
        )
        .first()
    )

    return query_response
