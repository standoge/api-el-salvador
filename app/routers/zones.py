from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.internal.crud as crud
import app.internal.schemas as schemas
from app.internal.db import db_connection

router = APIRouter()


# this functions keeps the same indentation due Black formatter
@router.get(path="/zones/{zone_name}", response_model=schemas.Zone, tags=["ZONES"])
def read_zone(zone_name: str, db: Session = Depends(db_connection)):
    """Return zone data in json format. Use lowercase and underscores instead of spaces (la_libertad instead of La Libertad).

    **Parameters:**\t
        `zone_name:` Name of country zone to get information about. It's include departments in.

    """
    db_zone = crud.get_zone(db, zone_name)
    return db_zone
