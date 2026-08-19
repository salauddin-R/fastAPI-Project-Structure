from sqlalchemy import BigInteger,Column,Double,TIMESTAMP,ForeignKey
from datetime import datetime,timezone
from sqlalchemy.orm import relationship

from models.base import Base

class Invoice(Base):
    __tablename__="invoices"
    
    id=Column(BigInteger,primary_key=True,autoincrement=True)
    user_id=Column(BigInteger,ForeignKey("users.id"),nullable=False)
    customer_id=Column(BigInteger,ForeignKey("customers.id"),nullable=False)
    total=Column(Double,nullable=False)
    discount=Column(Double,nullable=False)
    vat=Column(Double,nullable=False)
    payable=Column(Double,nullable=False)
                    
    create_at=Column(TIMESTAMP,nullable=False,default=lambda:datetime.now(timezone.utc))
    updated_at=Column(TIMESTAMP,nullable=False,default=lambda:datetime.now(timezone.utc),onupdate=lambda:datetime.now(timezone.utc))

    #Relationship
    users = relationship("user",back_populates="invoice")
    customers = relationship("Customer",back_populates="invoice")
    invoice_products = relationship("InvoiceProduct",back_populates="invoice")