from sqlalchemy import Column, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class ResponseProduct(Base):
    __tablename__ = "response_product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_response = Column(Integer, ForeignKey("response.id"))
    id_product = Column(Integer, ForeignKey("product.id"))

    def __repr__(self):
        return f"<ResponseProduct {self.id}, {self.id_response}, {self.id_product}>"
