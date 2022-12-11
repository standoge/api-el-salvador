from fastapi import HTTPException, Response
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

import app.internal.models as models
import json


def error_message(request):
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


@error_message
def get_departament(db: Session, dp_name: str):
    """Returns the first match with dp_name argument in depsv table."""
    query_response = (
        db.query(models.Departament)
        .filter(
            models.Departament.depname == dp_name,
        )
        .first()
    )

    return query_response


@error_message
def get_municipality(db: Session, mun_name: str):
    """Returns the first match with mun_name argument in munsv table."""
    query_response = (
        db.query(models.Municipality)
        .filter(models.Municipality.munname == mun_name)
        .first()
    )

    return query_response


@error_message
def get_zone(db: Session, zone_name: str):
    "Returns the first match with zone_name argument in zonesv table."
    query_response = (
        db.query(models.Zone).filter(models.Zone.zonename == zone_name).first()
    )

    return query_response