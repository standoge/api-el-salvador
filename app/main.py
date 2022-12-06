import uvicorn

from fastapi import FastAPI, Query, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, schemas
from db import db_connection


app = FastAPI()


@app.get("/")
def read_root():
    """Main endpoint"""


# dep is get it from search bar writing its name
@app.get("/departaments/{name}", response_model=schemas.Departament)
def read_departament(name: str, db: Session = Depends(db_connection)):
    """Returns departaments data in json format."""

    db_departament = crud.get_departament(db, name)

    if db_departament is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_departament


# dep is updated from <form> UI maybe
# @app.put("/departaments")
# def update_departament(departament: str = Body()):
#     """Update departaments information."""
#     ...


# equal than dep
@app.get("/townships")
def read_township(township: str = Query(min_length=5, max_length=19)):
    """Returns towships data in json format."""


# equal than dep
# @app.put("/townships")
# def update_township(
#     township: str = Body(),
# ):
#     ...


if __name__ == "__main__":

    uvicorn.run("main:app", reload=True)
