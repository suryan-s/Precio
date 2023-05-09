from fastapi import HTTPException, Request
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from backend import app
from backend.endpoints import insert_into_table_WMS, load_sql_to_pandas
from backend.schemas import WMSData


@app.post("/api/WMS/{api_token}")
async def update_wms(api_token: str, request: Request, data: WMSData):
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
    
@app.get("/api/WMS/Insight/{api_token}")
async def insight_load_sql(api_token: str) -> dict:
    try:
        print(api_token)
        status = load_sql_to_pandas(api_token)
        return status
    except Exception as e:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))