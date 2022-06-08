from sqlalchemy import Column, Integer, Float, ARRAY
from sqlalchemy.ext.declarative import declarative_base

from database import engine

Base = declarative_base()


class BBox(Base):
    __tablename__ = "bbox"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    bbox = Column(ARRAY[Float])

    def __repr__(self):
        return "<BBox %r, %r>" % self.id, self.bbox


Base.metadata.create_all(engine)
