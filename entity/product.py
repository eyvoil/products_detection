from sqlalchemy import Column, Integer, Float, Text, ForeignKey
from sqlalchemy.orm import relationship

from database import Base
from entity.response_product import ResponseProduct


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    product = Column(Text)
    probability = Column(Float)
    id_bbox = Column(Integer, ForeignKey("bbox.id"))
    bbox = relationship("BBox")
    id_product = relationship("Response", secondary='response_product', backref="product")

    def __repr__(self):
        return f"<Product {self.id}, {self.product}, {self.probability}, {self.bbox}>"
