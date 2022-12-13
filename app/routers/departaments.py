from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.internal.crud as crud
import app.internal.schemas as schemas
from app.internal.db import db_connection

router = APIRouter()


@router.get(
    path="/departaments/{dep_name}",
    response_model=schemas.Departament,
    tags=["DEPARTAMENTS"],
)
def read_departament(dep_name: str, db: Session = Depends(db_connection)):
    """Returns departaments data in json format."""

    db_departament = crud.get_departament(db, dep_name)
    return db_departament
