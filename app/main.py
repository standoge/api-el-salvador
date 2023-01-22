from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.internal.middlewares import SyntaxisErrorMiddleware, TimeMiddleware
from app.routers import departments, municipalities, scraper, zones

app = FastAPI()
app.title = "Maquilishuat"
app.version = "1.2.0"

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
