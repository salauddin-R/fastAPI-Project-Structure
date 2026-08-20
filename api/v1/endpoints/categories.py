from fastapi import APIRouter
router=APIRouter()

@router.post("/")
async def create_category():
    return{"message":"create_category"}

@router.get("/")
async def read_all_categories():
    return{"message":"read_categories"}

@router.get("/{category_id}")
async def read_categories():
    return{"message":"read_categories"}

@router.post("/{category_id}")
async def update_category():
    return{"message":"update_category"}

@router.delete("/{category_id}")
async def delete_category():
    return{"message":"delete_category"}