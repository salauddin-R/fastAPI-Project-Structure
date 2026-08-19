from sqlalchemy import BigInteger,Column,String,TIMESTAMP,ForeignKey
from datetime import datetime,timezone
from sqlalchemy.orm import relationship

from models.base import Base

class InvoiceProduct(Base):
    __tablename__="invoice_products"
    
    id=Column(BigInteger,primary_key=True,autoincrement=True)
    product_id=Column(BigInteger,ForeignKey("products.id"),nullable=False)
    invoice_id=Column(BigInteger,ForeignKey("invoices.id"),nullable=False)
    qty=Column(String,nullable=False)
    sale_price=Column(String,nullable=False)
                    
    create_at=Column(TIMESTAMP,nullable=False,default=lambda:datetime.now(timezone.utc))
    updated_at=Column(TIMESTAMP,nullable=False,default=lambda:datetime.now(timezone.utc),onupdate=lambda:datetime.now(timezone.utc))

    #Relationship
    users = relationship("user",back_populates="invoice_products")
    invoices = relationship("Invoice",back_populates="invoice_products")
    products = relationship("Product",back_populates="invoice_products")