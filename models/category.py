from sqlalchemy import BigInteger,Column,String,TIMESTAMP,ForeignKey
from datetime import datetime,timezone
from sqlalchemy.orm import relationship

from models.base import Base

class Category(Base):
    __tablename__="categories"
    
    id=Column(BigInteger,primary_key=True,autoincrement=True)
    name=Column(String,nullable=False)
    user_id=Column(BigInteger,ForeignKey("users.id"),nullable=False)
                    
    create_at=Column(TIMESTAMP,nullable=False,default=lambda:datetime.now(timezone.utc))
    updated_at=Column(TIMESTAMP,nullable=False,default=lambda:datetime.now(timezone.utc),onupdate=lambda:datetime.now(timezone.utc))

    #Relationship
    products = relationship("Product",back_populates="category")
    users = relationship("user",back_populates="category")
        