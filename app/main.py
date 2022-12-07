import uvicorn

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud, schemas
from db import db_connection


app = FastAPI()


@app.get("/")
def read_root():
    """Main endpoint"""
    return {"Hello": "From FastAPI"}


@app.get("/departaments/{dep_name}", response_model=schemas.Departament)
def read_departament(dep_name: str, db: Session = Depends(db_connection)):
    """Returns departaments data in json format."""

    db_departament = crud.get_departament(db, dep_name)
    return db_departament


@app.get("/townships/{mun_name}", response_model=schemas.Township)
def read_township(mun_name: str, db: Session = Depends(db_connection)):
    """Returns towships data in json format."""

    db_township = crud.get_township(db, mun_name)
    return db_township

@app.get("/zones/{zone_name}", response_model=schemas.Zone)
def read_township(zone_name: str, db: Session = Depends(db_connection)):
        """Returns zone data in json format"""
        db_zone = crud.get_zone(db, zone_name)
        return db_zone

if __name__ == "__main__":

    uvicorn.run("main:app", reload=True)
