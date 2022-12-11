from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.internal.crud as crud, app.internal.schemas as schemas
from app.internal.db import db_connection

router = APIRouter()


@router.get("/zones/{zone_name}", response_model=schemas.Zone, tags=["zones"])
def read_zone(zone_name: str, db: Session = Depends(db_connection)):
    """Returns zone data in json format"""

    db_zone = crud.get_zone(db, zone_name)
    return db_zone
