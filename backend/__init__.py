import mimetypes

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/css", ".css")

app = FastAPI(
    title="Precio",
    version="1.0.0",
    contact={"name": "S Suryan", "email": "suryannasa@gmail.com"},
    description="""
    Precio is an open-source software tool for monitoring,
    automating and visualizing farming data. It provides
    real-time data analysis and insights of farming,
    enabling informed decision-making and improving farming efficiency.
    """,
    license_info={"name": "MIT"},
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import backend.api
import backend.endpoints
import backend.pms
import backend.schemas
import backend.wms
