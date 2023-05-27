from fastapi import APIRouter, HTTPException, Request

from backend.endpoints import insert_into_table_PMS

router = APIRouter()

@router.post("/api/PMS/{api_token}")
async def update_pms(api_token: str, request: Request) -> dict:
    """
    Updates the PMS (Plant Monitoring System) using the provided API token and request data.

    Args:
        api_token (str): The API token used for operations with table
        request (Request): The FastAPI request object containing the incoming data.

    Returns:
        dict: A dictionary containing the status of the update operation.

    Raises:
        HTTPException: If an error occurs during the update operation, an HTTPException with a 500 status code and
                       a detailed error message will be raised.

    Usage:
        This endpoint is used to update the Plant Monitoring System (PMS) by providing the necessary API token
        and request data. The provided API token is used to access the table. The request
        data should be in JSON format and should contain the necessary information for the update operation.

        The function 'insert_into_table_PMS' is called to perform the actual update operation with the incoming data
        and API token. The returned status of the update operation is then encapsulated in a dictionary and returned
        as the response.

        If any exception occurs during the update operation, it will be caught, and an HTTPException with a 500
        status code and a detailed error message will be raised.

    Note:
        - This function assumes that the 'insert_into_table_PMS' function is defined and implemented elsewhere.
        - The actual implementation of this function may vary depending on the specific requirements and
          implementation details.

    """
    try:
        incoming = await request.json()
        print(incoming)
        print(api_token)
        status = insert_into_table_PMS(incoming, api_token)
        return {"status": status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))