from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

import app.internal.crud as crud
import app.internal.schemas as schemas
from app.internal.db import db_connection

router = APIRouter()


@router.get(
    path="/municipalities/{mun_name}",
    response_model=schemas.Municipality,
    tags=["MUNICIPALITIES"],
)
def read_municipality(
    mun_name: str,
    db: Session = Depends(db_connection),
    departament: Optional[str] = Query(default=None, min_length=6, max_length=12),
):
    """Return municipalities data in json format.

    `Args:`\t
        **mun_name:** Name of municipalitie to get information about.\t
        **departament:** Optional argument, some municipalities got equal names across departmnets.
                     Use it to specify a specifiq municipalitie from specifiq deparment.

    """
    if departament is not None:
        db_municipality_by_dp = crud.get_municipality_by_dep(db, mun_name, departament)
        return db_municipality_by_dp

    db_municipality = crud.get_municipality(db, mun_name)
    return db_municipality
