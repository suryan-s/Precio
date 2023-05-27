from fastapi import APIRouter, HTTPException, Request
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from backend.endpoints import insert_into_table_WMS, load_sql_to_pandas
from backend.schemas import WMSData

router = APIRouter()

@router.post("/api/WMS/{api_token}")
async def update_wms(api_token: str, request: Request, data: WMSData):
    """
    Updates WMS(Weather Monitoring System) data in the database.

    Args:
        api_token (str): The API token for authentication.
        request (Request): The HTTP request object.
        data (WMSData): The data to be updated in the WMS table.

    Returns:
        dict: A dictionary containing the status of the update operation.

    Raises:
        HTTPException: If the project is not found (status code 404) or if an internal server error occurs (status code 500).
    """
    try:
        incoming = await request.json()
        print(incoming)
        print(api_token)
        status = insert_into_table_WMS(incoming, api_token)
        if status == 200:
            return {"status": status}
        if status == 404:
            raise HTTPException(status_code=404, detail="No such project found!")
    except Exception as error:
        print("Exception-update_wms : ", error)
        raise HTTPException(status_code=500, detail=str(error))


@router.get("/api/WMS/Insight/{api_token}")
async def insight_load_sql(api_token: str) -> dict:
    """
    Loads WMS data from the database using a SQL query.

    Args:
        api_token (str): The API token for authentication.

    Returns:
        dict: A dictionary containing the loaded data.

    Raises:
        HTTPException: If an internal server error occurs (status code 500).
    """
    try:
        print(api_token)
        status = load_sql_to_pandas(api_token)
        return status
    except Exception as error:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
