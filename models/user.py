from sqlalchemy import BigInteger,Column,String,TIMESTAMP
from datetime import datetime,timezone
from sqlalchemy.orm import relationship

from models.base import Base
class User(Base):
    __tablename__="users"

    id=Column(BigInteger,primary_key=True,autoincrement=True)
    fastName=Column(String,nullable=False)
    lastName=Column(String,nullable=False)
    email=Column(String,nullable=False,unique=True)
    mobile=Column(String,nullable=False)
    password=Column(String,nullable=False)
    otp=Column(String,nullable=False)
    create_at=Column(TIMESTAMP,nullable=False,default=lambda:datetime.now(timezone.utc))
    updated_at=Column(TIMESTAMP,nullable=False,default=lambda:datetime.now(timezone.utc),onupdate=lambda:datetime.now(timezone.utc))

    #Relationship
    categories = relationship("Category",back_populates="user")
    products = relationship("Product",back_populates="user")
    invoices = relationship("Invoice",back_populates="user")
    invoice_products = relationship("InvoiceProduct",back_populates="user")
    customers = relationship("Customer",back_populates="user")
