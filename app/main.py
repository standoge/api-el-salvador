from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import departaments, municipalities, zones, scrapper

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["get"],
)

# routes
app.include_router(departaments.router)
app.include_router(municipalities.router)
app.include_router(zones.router)
app.include_router(scrapper.router)


@app.get("/")
def read_root():
    """Main endpoint"""
    return {"Hello": "From FastAPI"}
