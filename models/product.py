from sqlalchemy import BigInteger,Column,String,TIMESTAMP,ForeignKey
from datetime import datetime,timezone
from sqlalchemy.orm import relationship

from models.base import Base

class Product(Base):
    __tablename__="products"
    
    id=Column(BigInteger,primary_key=True,autoincrement=True)
    user_id=Column(BigInteger,ForeignKey("users.id"),nullable=False)
    name=Column(String,nullable=False)
    price=Column(String,nullable=False)
    unit=Column(String,nullable=False)
    img_url=Column(String,nullable=False)
                    
    create_at=Column(TIMESTAMP,nullable=False,default=lambda:datetime.now(timezone.utc))
    updated_at=Column(TIMESTAMP,nullable=False,default=lambda:datetime.now(timezone.utc),onupdate=lambda:datetime.now(timezone.utc))

    #Relationship
    users = relationship("user",back_populates="product")
    categories = relationship("Category",back_populates="product")
    invoice_products = relationship("InvoiceProduct",back_populates="product")
    