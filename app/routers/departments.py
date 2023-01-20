from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.internal.crud as crud
import app.internal.schemas as schemas
from app.internal.db import db_connection

router = APIRouter()


@router.get(
    path="/departments/{dep_name}",
    response_model=schemas.Department,
    tags=["DEPARTMENTS"],
)
def read_departament(dep_name: str, db: Session = Depends(db_connection)):
    """Return departments data in json format.

    `Args:`\t
        **dep_name:** Name of department to get information about

    """
    db_department = crud.get_department(db, dep_name)
    return db_department
