from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import departments, municipalities, zones, scraper
from app.internal.middlewares import SyntaxisErrorMiddleware, TimeMiddleware

app = FastAPI()
app.title = "Maquilishuat"
app.version = "1.1.1"

origins = ["*"]

# middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["get"],
)
app.add_middleware(SyntaxisErrorMiddleware)
app.add_middleware(TimeMiddleware)

# routes
app.include_router(departments.router)
app.include_router(municipalities.router)
app.include_router(zones.router)
app.include_router(scraper.router)


@app.get("/")
def read_root():
    """Main endpoint"""
    return {"Hello": "From FastAPI"}
