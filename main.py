import mimetypes

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

from endpoints import *

mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')

# http://192.168.239.143:8000/static/
# To start the server run the following command: uvicorn main:app --reload     
# (main is the name of the file and app is the name of the variable)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static/", StaticFiles(directory="./frontend/dist", html=True), name="static")

# @app.get("/", response_class=HTMLResponse)
# async def read_index():
#     with open(r"frontend\build\index.html", "r") as index_file:
#         return index_file.read()

@app.get("/")
async def read_index():
    return RedirectResponse(url="static")
    
@app.post("/api/condevice")
async def connect_(request : Request):
    incoming = await request.json()
    return get_client(incoming)

@app.get("/api/test")
async def connect(request : Request):
    print("Called status")
    return {"message": "Server up and running"}

@app.post("/api/createProject")
async def create_table(request : Request):
    incoming = await request.json()
    incoming = json.dumps(incoming)
    incoming = json.loads(incoming)
    status = create_project(incoming)
    return {"status": status}

@app.post("/api/deleteProject/{api_token}")
async def deleteProject(api_token : str):
    status = None
    status = delete_project(api_token) 
    print("Status",status)
    return {"status": status}

@app.post("/api/WMS/{api_token}")
async def update_wms(api_token : str, request : Request):
    incoming = await request.json()
    incoming = json.dumps(incoming)
    incoming = json.loads(incoming)
    print(incoming)
    print(api_token)
    status = insert_into_table_WMS(incoming, api_token)
    return {"status": status}

@app.post("/api/PMS/{api_token}")
async def update_pms(api_token : str, request : Request):
    incoming = await request.json()
    incoming = json.dumps(incoming)
    incoming = json.loads(incoming)
    print(incoming)
    print(api_token)
    status = insert_into_table_PMS(incoming, api_token)
    return {"status": status}
    
@app.get("/api/getTableNames")
async def get_table():
    return get_table_names()    

@app.get("/api/getLineGraph/{api_token}/{graph}")
async def get_graph(api_token : str, graph : int):
    return get_line_data(api_token, graph)

@app.get("/api/getGauge/{api_token}")
async def get_gauge(api_token : str):
    return get_gauge_data(api_token)
@app.get("/api/predict/basic")
async def predict_basic():
    return predictBasic()