from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from endpoints import *


app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("index.html", "r") as index_file:
        return index_file.read()
    
@app.post("/api/condevice")
async def connect_(request : Request):
    incoming = await request.json()
    return get_client(incoming)

@app.get("/api/test")
async def connect(request : Request):
    return {"message": "Server up and running"}

@app.post("/api/createProject")
async def create_table(request : Request):
    incoming = await request.json()
    incoming = json.dumps(incoming)
    incoming = json.loads(incoming)
    status = create_project(incoming)
    return {"status": status}

@app.post("/api/update/{api_token}")
async def update_table(api_token : str, request : Request):
    incoming = await request.json()
    incoming = json.dumps(incoming)
    incoming = json.loads(incoming)
    print(incoming)
    print(api_token)
    status = insert_into_table(incoming)
    return {"status": status}
    
    