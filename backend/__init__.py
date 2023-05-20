"""
Precio

An open-source software tool for monitoring, automating, and visualizing farming data.
This program utilizes the FastAPI framework and provides real-time data analysis and insights of farming, enabling informed decision-making and improving farming efficiency.

Modules:
    - backend.api: Contains routes for FastAPI.
    - backend.endpoints: Defines the endpoints for the API.
    - backend.pms: Provides functionality for the Plant Monitoring System.
    - backend.schemas: Contains data schemas and models for the API.
    - backend.wms: Provides functionality for the Weather Monitoring System.
"""

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
