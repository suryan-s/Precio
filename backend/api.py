
"""
This module contains the FastAPI endpoints for the application.

Functions:
- connect_: Handles the POST request to '/api/condevice' endpoint. Retrieves client information.
- connect: Handles the GET request to '/api/test' endpoint. Returns a status message.
- create_table: Handles the POST request to '/api/createProject' endpoint. Creates a project table.
- delete_table: Handles the POST request to '/api/deleteProject/{api_token}' endpoint. Deletes a project table.
- get_table: Handles the GET request to '/api/getTableNames' endpoint. Retrieves table names.
- get_graph: Handles the GET request to '/api/getLineGraph/{api_token}/{graph}' endpoint. Retrieves line graph data.
- get_gauge: Handles the GET request to '/api/getGauge/{api_token}' endpoint. Retrieves gauge data.
- predict_basic: Handles the GET request to '/api/predict/basic' endpoint. Performs a basic prediction.

Exceptions:
- HTTPException: Raised when an internal server error occurs.

"""
from fastapi import APIRouter, HTTPException, Request
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from backend.endpoints import (create_project, create_tables, delete_project,
                               get_client, get_gauge_data, get_line_data,
                               get_table_names, predictBasic)

router = APIRouter()

@router.on_event("startup")
async def startup():
    await create_tables()
    print("Startup complete")

@router.post("/api/condevice")
async def connect_(request: Request):
    try:
        incoming = await request.json()
        return get_client(incoming)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/api/test")
async def connect() -> dict:
    try:
        print("Called status")
        return {"message": "Server up and running"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/api/createProject")
async def create_table(request: Request) -> dict:
    try:
        incoming = await request.json()
        status = await create_project(incoming)
        return {"status": status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/api/deleteProject/{api_token}")
async def delete_table(api_token: str):
    try:
        # status = None
        status = await delete_project(api_token)
        print("Status: ", status)
        return {"status": status}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/api/getTableNames")
async def get_table():
    try:
        return await get_table_names()
    except Exception as e:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/api/getLineGraph/{api_token}/{graph}")
async def get_graph(api_token: str, graph: int):
    try:
        result = await get_line_data(api_token, graph)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/api/getGauge/{api_token}")
async def get_gauge(api_token: str):
    try:
        return await get_gauge_data(api_token)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/api/predict/basic")
async def predict_basic():
    try:
        return predictBasic()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


