"""
This module contains the FastAPI endpoints for the application.

Functions:
- connect_: Handles the POST request to '/api/condevice' endpoint. Retrieves client information.
- connect: Handles the GET request to '/api/test' endpoint. Returns a status message.
- create_table: Handles the POST request to '/api/createProject' endpoint. Creates a project table.
- delete_table: Handles the POST request to '/api/deleteProject/{api_token}' endpoint. 
                Deletes a project table.
- get_table: Handles the GET request to '/api/getTableNames' endpoint. Retrieves table names.
- get_graph: Handles the GET request to '/api/getLineGraph/{api_token}/{graph}' endpoint. 
            Retrieves line graph data.
- get_gauge: Handles the GET request to '/api/getGauge/{api_token}' endpoint. Retrieves gauge data.
- predict_basic: Handles the GET request to '/api/predict/basic' endpoint. 
                Performs a basic prediction.

Exceptions:
- HTTPException: Raised when an internal server error occurs.

"""
from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

from backend.auth import get_user_id_from_token

from backend.endpoints import (
    create_project,
    create_tables,
    delete_project,
    get_client,
    get_gauge_data,
    get_line_data,
    get_table_names,
    predictBasic,
)
from backend.schemas import CreateProject

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_token(token: str = Depends(oauth2_scheme)):
    """
    Returns the current token.
    :param token:
    :return: token
    """
    if not token:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing authorization token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token


@router.on_event("startup")
async def startup():
    """
    Performs startup tasks.

    This function is executed when the application starts up. It calls the `create_tables` function
    to create necessary database tables.

    Args:
        None

    Returns:
        None
    """
    await create_tables()
    # print("Startup complete")


@router.post("/api/condevice")
async def connect_(request: Request):
    """
    Connects to a device and retrieves data.

    This route handles a POST request to connect to a device specified in the request payload.
    It calls the `get_client` function to retrieve data from the device.

    Args:
        request: The request object containing the payload with device information.

    Returns:
        The response containing the retrieved data.
    """
    try:
        incoming = await request.json()
        return get_client(incoming)
    except Exception as error:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error"
        ) from error


@router.get("/api/test")
async def connect() -> dict:
    """
    Returns a test message indicating the server is up and running.

    This route handles a GET request to test the server's connectivity.

    Args:
        None

    Returns:
        A dictionary containing the test message.
    """
    try:
        print("Called status")
        return {"message": "Server up and running"}
    except Exception as error:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error"
        ) from error


@router.post("/api/createProject")
async def create_table(request: Request, project: CreateProject, token: str = Depends(get_current_token)) -> dict:
    """
    Creates a new project table in the database.

    This route handles a POST request to create a new project table in the database.
    It calls the `create_project` function to create the project table.

    Args:
        request: The request object containing the payload with project information.

    Returns:
        A dictionary containing the status of the operation.
        :param token:
        :param request:
        :param project: Model for project
    """
    user_id = await get_user_id_from_token(token)
    if user_id is None:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing authorization token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    incoming = await request.json()
    status = await create_project(incoming, user_id)
    if status == 500:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error"
        )
    return {"status": status}


@router.post("/api/deleteProject/{project_id}")
async def delete_table(project_id: str, token: str = Depends(get_current_token)):
    """
    Deletes a project table from the database.

    This route handles a POST request to delete a project table specified by the `api_token`.
    It calls the `delete_project` function to delete the project table.

    Args:
        project_id: The API token of the project table to be deleted.

    Returns:
        A dictionary containing the status of the operation.
        :param project_id:
        :param token:
    """
    user_id = await get_user_id_from_token(token)
    if user_id is None:
        raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Invalid or missing authorization token",
                headers={"WWW-Authenticate": "Bearer"},
        )
    status = await delete_project(project_id, user_id)
    if status == 500:
        raise HTTPException(
                status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error"
        )
    return {"status": status}


@router.get("/api/getTableNames")
async def get_table(token: str = Depends(get_current_token)):
    """
    Retrieves the names of all project tables in the database.

    This route handles a GET request to retrieve the names of all project tables in the database.
    It calls the `get_table_names` function to retrieve the table names.

    Args:
        None

    Returns:
        A list of table names.
        :param token:
    """
    user_id = await get_user_id_from_token(token)
    if user_id is None:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing authorization token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    result, status = await get_table_names(user_id)
    if result is None:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="No projects found"
        )
    else:
        return {"result": result, "status": status}


@router.get("/api/getLineGraph/{api_token}/{graph}")
async def get_graph(api_token: str, graph: int):
    """
    Retrieves data for a line graph.

    This route handles a GET request to retrieve data for a line graph specified by
    the `api_token` and `graph` parameters.
    It calls the `get_line_data` function to retrieve the graph data.

    Args:
        api_token: The API token of the project table.
        graph: The graph identifier.

    Returns:
        The retrieved data for the line graph.
    """
    try:
        result = await get_line_data(api_token, graph)
        return result
    except Exception as error:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error"
        ) from error


@router.get("/api/getGauge/{api_token}")
async def get_gauge(api_token: str):
    """
    Retrieves data for a gauge.

    This route handles a GET request to retrieve data for a gauge
    specified by the `api_token` parameter.
    It calls the `get_gauge_data` function to retrieve the gauge data.

    Args:
        api_token: The API token of the project table.

    Returns:
        The retrieved data for the gauge.
    """
    try:
        return await get_gauge_data(api_token)
    except Exception as error:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error"
        ) from error


@router.get("/api/predict/basic")
async def predict_basic():
    """
    Performs a basic prediction.

    This route handles a GET request to perform a basic prediction.
    It calls the `predictBasic` function to perform the prediction.

    Args:
        None

    Returns:
        The prediction result.
    """
    try:
        return predictBasic()
    except Exception as error:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error"
        ) from error