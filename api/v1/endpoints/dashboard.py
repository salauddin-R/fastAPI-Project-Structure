from fastapi import APIRouter
router=APIRouter()

@router.get("/")
async def get_dashboard():
    return{"message":"Dashboard"}

@router.get("/starts")
async def get_dashboard_starts():
    return{"message":"get_dashboard_starts"}

@router.post("/recent_activities")
async def recent_activities():
    return{"message":"recent_activities"}
