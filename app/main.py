import uvicorn

from fastapi import FastAPI, Query, Body

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/")
def get_departament(
        departament: str = Query(),
    ):
    ...

@app.patch("/")
def update_departament(
        departament: str = Body(),
    ):
    ...

@app.get("/")
def get_township(
        township: str = Query(),
    ):
    ...

@app.patch("/")
def update_township(
        township: str = Body(),
    ):
    ...

if __name__ == "__main__":

    uvicorn.run("main:app")

