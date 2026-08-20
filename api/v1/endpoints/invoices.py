from fastapi import APIRouter
router=APIRouter()

@router.post("/")
async def create_invoice():
    return{"message":"create_invoice"}

@router.get("/")
async def read_all_invoice():
    return{"message":"read_all_invoice"}

@router.get("/{invoice_id}")
async def read_invoice():
    return{"message":"invoice_id"}

@router.post("/{invoice_id}")
async def update_invoice():
    return{"message":"update_invoice"}

@router.delete("/{invoice_id}")
async def delete_invoice():
    return{"message":"delete_invoice"}