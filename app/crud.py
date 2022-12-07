from fastapi import HTTPException
from sqlalchemy.orm import Session

import models


def error_message(request):
    """Raise exception when path argument isn't in db"""

    def wrapper(*args):
        """Wrap query db function to handle exception"""
        response = request(*args)
        if response is None:
            raise HTTPException(status_code=404, detail="That values doesn't exists")
        return response

    return wrapper


@error_message
def get_departament(db: Session, dp_name: str):
    """Returns the first match with dp_name argument in depsv table."""
    query_response = (
        db.query(models.Departament)
        .filter(models.Departament.depname == dp_name)
        .first()
    )

    return query_response


@error_message
def get_township(db: Session, mun_name: str):
    """Returns the first match with tws_name argument in munsv table."""
    query_response = (
        db.query(models.Township).filter(models.Township.munname == mun_name).first()
    )

    return query_response
