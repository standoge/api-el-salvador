import uvicorn

from fastapi import FastAPI, Query, Body

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# dep is get it from search bar writing its name
@app.get("/")
def get_departament(departament: str = Query(min_length=5, max_length=10)):
    ...


# dep is updated from <form> UI maybe
@app.patch("/")
def update_departament(departament: str = Body()):
    ...


# equal than dep
@app.get("/")
def get_township(township: str = Query(min_length=5, max_length=19)):
    ...


# equal than dep
@app.patch("/")
def update_township(
    township: str = Body(),
):
    ...


if __name__ == "__main__":

    uvicorn.run("main:app")
