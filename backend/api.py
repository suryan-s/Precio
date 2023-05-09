
from fastapi import HTTPException, Request
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from backend import app
from backend.endpoints import *
from backend.schemas import *


@app.post("/api/condevice")
async def connect_(request: Request):
    try:
        incoming = await request.json()
        return get_client(incoming)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/test")
async def connect() -> dict:
    try:
        print("Called status")
        return {"message": "Server up and running"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/createProject")
async def create_table(request: Request) -> dict:
    try:
        incoming = await request.json()
        status = create_project(incoming)
        return {"status": status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/deleteProject/{api_token}")
async def delete_table(api_token: str):
    try:
        # status = None
        status = delete_project(api_token)
        print("Status: ", status)
        return {"status": status}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/getTableNames")
async def get_table():
    try:
        return get_table_names()
    except Exception as e:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@app.get("/api/getLineGraph/{api_token}/{graph}")
async def get_graph(api_token: str, graph: int):
    try:
        return get_line_data(api_token, graph)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/getGauge/{api_token}")
async def get_gauge(api_token: str):
    try:
        return get_gauge_data(api_token)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/predict/basic")
async def predict_basic():
    try:
        return predictBasic()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


