from fastapi import APIRouter
router=APIRouter()

@router.post("/")
async def create_products():
    return{"message":"create_products"}

@router.get("/")
async def read_all_products():
    return{"message":"read_all_products"}

@router.get("/{products_id}")
async def read_products():
    return{"message":"products_id"}

@router.post("/{products_id}")
async def update_products():
    return{"message":"update_products"}

@router.delete("/{products_id}")
async def delete_products():
    return{"message":"delete_products"}