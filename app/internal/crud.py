from fastapi import HTTPException, Response
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

import app.internal.models as models
import json


def query_error(request):
    """Raise exception when path argument isn't in db"""

    def wrapper(*args):
        """Wrap query db function to handle exception"""
        response = request(*args)
        if response is None:
            raise HTTPException(status_code=404, detail="That values doesn't exists")

        json_response = Response(
            content=json.dumps(jsonable_encoder(response), indent=4, default=str),
            media_type="application/json",
        )

        return json_response

    return wrapper


@query_error
def get_department(db: Session, dp_name: str):
    """Return the first match with dp_name argument in depsv table."""
    query_response = (
        db.query(models.Department)
        .filter(
            models.Department.depname == dp_name,
        )
        .first()
    )

    return query_response


@query_error
def get_municipality(db: Session, mun_name: str):
    """Return the first match with mun_name argument in munsv table."""
    query_response = (
        db.query(models.Municipality)
        .filter(models.Municipality.munname.like(f"{mun_name}%"))
        .all()
    )

    return query_response


@query_error
def get_municipality_by_dep(db: Session, mun_name: str, dep_name: str):
    """Return the first match with mun_name in munsv table."""
    query_response = (
        db.query(models.Municipality)
        .filter(
            models.Municipality.munname.like(f"{mun_name}%"),
            models.Municipality.department.has(models.Department.depname == dep_name),
        )
        .first()
    )

    return query_response


@query_error
def get_zone(db: Session, zone_name: str):
    """Return the first match with zone_name argument in zonesv table."""
    query_response = (
        db.query(models.Zone).filter(models.Zone.zonename == zone_name).first()
    )

    return query_response