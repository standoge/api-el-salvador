from fastapi import FastAPI
from app.routers import departaments, municipalities, zones


app = FastAPI()


# routes
app.include_router(departaments.router)
app.include_router(municipalities.router)
app.include_router(zones.router)


@app.get("/")
def read_root():
    """Main endpoint"""
    return {"Hello": "From FastAPI"}
