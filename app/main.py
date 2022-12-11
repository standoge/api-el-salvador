import uvicorn

from fastapi import FastAPI
from app.routers import departaments, municipalities, zones


app = FastAPI()


app.include_router(departaments.router)
app.include_router(municipalities.router)
app.include_router(zones.router)


@app.get("/")
def read_root():
    """Main endpoint"""
    return {"Hello": "From FastAPI"}


# if __name__ == "__main__":

    # uvicorn.run("main:app", reload=True)
