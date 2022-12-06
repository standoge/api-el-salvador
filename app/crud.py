from sqlalchemy.orm import Session

import models
import schemas


def get_departament(db: Session, dp_name: str):
    return (
        db.query(models.Departament).filter(models.Departament.name == dp_name).first()
    )
