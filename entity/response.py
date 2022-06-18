from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.orm import relationship

from database import Base
from entity.response_product import ResponseProduct


class Response(Base):
    __tablename__ = "response"

    id = Column(Integer, primary_key=True, autoincrement=True)
    response_date = Column(DateTime)
    id_product = relationship("Product", secondary="response_product", backref="response")

    def __repr__(self):
        return f"<Response {self.id}, {self.response_date}>"
