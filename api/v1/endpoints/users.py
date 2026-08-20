from fastapi import APIRouter
router=APIRouter()

@router.post("/")
async def create_users():
    return{"message":"create_users"}

@router.get("/")
async def read_all_users():
    return{"message":"read_all_users"}

@router.get("/{users_id}")
async def read_users():
    return{"message":"users_id"}

@router.post("/{users_id}")
async def update_users():
    return{"message":"update_users"}

@router.delete("/{users_id}")
async def delete_users():
    return{"message":"delete_users"}