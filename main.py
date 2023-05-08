import mimetypes
import socket

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

from endpoints import *
from validation_form import *

mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')

# http://192.168.239.143:8000/static/
# http://127.0.0.1:8000/static/
# To start the server run the following command: uvicorn main:app --reload
# (main is the name of the file and app is the name of the FastAPI object)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static/", StaticFiles(directory="./frontend/dist", html=True), name="static")


def get_public_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


print(get_public_ip())


@app.get("/")
async def read_index():
    try:
        return RedirectResponse(url="static")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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
async def delete_project(api_token: str) -> dict:
    try:
        # status = None
        status = delete_project(api_token)
        print("Status", status)
        return {"status": status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/WMS/{api_token}")
async def update_wms(api_token: str, request: Request, data: WMSData):
    # status = None
    try:
        incoming = await request.json()
        print(incoming)
        print(api_token)
        status = insert_into_table_WMS(incoming, api_token)
        if status == 200:
            return {"status": status}
        elif status == 404:
            raise HTTPException(status_code=404, detail="No such project found!")
    except Exception as e:
        print("Exception-update_wms : ", e)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/PMS/{api_token}")
async def update_pms(api_token: str, request: Request) -> dict:
    try:
        incoming = await request.json()
        print(incoming)
        print(api_token)
        status = insert_into_table_PMS(incoming, api_token)
        return {"status": status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/Insight/{api_token}")
async def insight_load_sql(api_token: str) -> dict:
    try:
        print(api_token)
        status = load_sql_to_pandas(api_token)
        return status
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/getTableNames")
async def get_table():
    try:
        return get_table_names()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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
