from sqlalchemy.orm import Session

import models


def get_departament(db: Session, dp_name: str):
    return (
        db.query(models.Departament)
        .filter(models.Departament.depname == dp_name)
        .first()
    )
