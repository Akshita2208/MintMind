from fastapi import APIRouter, Depends
from services.db import report_collection
from auth.jwt_handler import get_current_user
from bson import ObjectId

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])

@router.get("/")
async def get_dashboard(user_id: str = Depends(get_current_user)):
    reports = []
    cursor = report_collection.find({"user_id": user_id}).sort("created_at", -1)
    async for doc in cursor:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        reports.append(doc)
    return {"status": "success", "reports": reports}
