from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.internal.crud as crud, app.internal.schemas as schemas
from app.internal.db import db_connection

router = APIRouter()


@router.get(
    "/municipalities/{mun_name}",
    response_model=schemas.Municipality,
    tags=["municipalities"]
)
def read_municipality(mun_name: str, db: Session = Depends(db_connection)):
    """Returns towships data in json format."""

    db_municipality = crud.get_municipality(db, mun_name)
    return db_municipality
