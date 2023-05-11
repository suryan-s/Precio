
from fastapi import HTTPException
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from backend import app

# http://192.168.239.143:8000/static/
# http://127.0.0.1:8000/static/
# To start the server run the following command: uvicorn main:app --reload
# (main is the name of the file and app is the name of the FastAPI object)

app.mount(
    "/static/", StaticFiles(directory="./frontend/dist", html=True), name="static"
)


@app.get("/")
async def read_index():
    try:
        return RedirectResponse(url="static")
    except Exception as e:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    host = "127.0.0.1"
    uvicorn.run("main:app", port=8000, host=host, workers=3)
