from fastapi import APIRouter
router=APIRouter()

@router.post("/")
async def create_customers():
    return{"message":"create_customers"}

@router.get("/")
async def read_all_customers():
    return{"message":"read_customers"}

@router.get("/{customers_id}")
async def read_customers():
    return{"message":"read_customers"}

@router.post("/{customers_id}")
async def update_customers():
    return{"message":"update_customers"}

@router.delete("/{customers_id}")
async def delete_customers():
    return{"message":"delete_customers"}