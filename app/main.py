import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("")
def get_departament():
    ...

@app.put("")
def update_departament():
    ...

@app.get("")
def get_township():
    ...

@app.put("")
def update_township():
    ...

if __name__ == "__main__":

    uvicorn.run("main:app")

