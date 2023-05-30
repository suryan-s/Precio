"""
Module to serve a FastAPI application with static files Uvicorn.

The module sets up a FastAPI application and mounts a directory
containing static files using the Starlette `StaticFiles` class.

The root URL ("/") is handled to redirect to the static files.

The application can be started using the Uvicorn server by running
the command: uvicorn main:app --reload

Usage:
    python main.py

Dependencies:
    - uvicorn
    - fastapi
    - starlette

"""
import uvicorn
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
    """
    Handles the root URL ("/") to redirect to the static files.
    This function redirects the root URL to the static files served
    from the "/static/" URL.   

    Returns:
        RedirectResponse: Redirects to the static files.

    Raises:
        HTTPException:
            The status code is set to HTTP 500 Internal Server Error,
            and the detail contains the error message.

    """
    try:
        return RedirectResponse(url="static")
    except Exception as error:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
            ) from error


if __name__ == "__main__":
    HOST = "127.0.0.1"
    uvicorn.run("main:app", port=8000, host=HOST, reload=True)
