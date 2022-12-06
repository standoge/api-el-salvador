import uvicorn

from fastapi import FastAPI, Query, Body, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from db import SessionLocal

app = FastAPI()


def db_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# dep is get it from search bar writing its name
@app.get("/departaments/{name}", response_model=schemas.Departament)
def read_departament(name: str, db: Session = Depends(db_connection)):

    db_departament = crud.get_departament(db, name)

    if db_departament is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_departament


# dep is updated from <form> UI maybe
@app.put("/departaments")
def update_departament(departament: str = Body()):
    ...


# equal than dep
@app.get("/townships")
def get_township(township: str = Query(min_length=5, max_length=19)):
    ...


# equal than dep
@app.put("/townships")
def update_township(
    township: str = Body(),
):
    ...


if __name__ == "__main__":

    uvicorn.run("main:app", reload=True)
