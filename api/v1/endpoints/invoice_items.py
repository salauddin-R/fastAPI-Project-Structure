from fastapi import APIRouter
router=APIRouter()

@router.post("/")
async def create_invoice_itmes():
    return{"message":"create_invoice_itmes"}

@router.get("/")
async def read_all_invoice_itmes():
    return{"message":"read_all_invoice_itmes"}

@router.get("/{invoice_itmes_id}")
async def read_invoice_itmes():
    return{"message":"invoice_itmes_id"}

@router.post("/{invoice_itmes_id}")
async def update_invoice_itmesy():
    return{"message":"update_invoice_itmes"}

@router.delete("/{invoice_itmes_id}")
async def delete_invoice_itmes():
    return{"message":"delete_invoice_itmes"}