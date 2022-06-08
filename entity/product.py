from sqlalchemy import Column, Integer, Float, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from database import engine

Base = declarative_base()


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    product = Column(Text)
    probability = Column(Float)
    id_bbox = Column(Integer, ForeignKey("bbox.id"))

    def __repr__(self):
        return "<Product %r, %r, %r, %r>" % self.id, self.product, self.probability, self.id_bbox


Base.metadata.create_all(engine)
