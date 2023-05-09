from fastapi import HTTPException, Request

from backend import app
from backend.endpoints import insert_into_table_PMS


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