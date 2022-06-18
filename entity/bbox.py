from sqlalchemy import Column, Integer, Float, ARRAY

from database import Base



class BBox(Base):
    __tablename__ = "bbox"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    bbox = Column(ARRAY(Float))

    def __repr__(self):
        return f"<BBox {self.id}, {self.bbox}>"
