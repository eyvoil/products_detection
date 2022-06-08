from sqlalchemy import Column, Text, LargeBinary, DateTime
from sqlalchemy.ext.declarative import declarative_base

from database import engine

Base = declarative_base()


class Request(Base):
    __tablename__ = "request"

    id = Column(Text, primary_key=True)
    img = Column(LargeBinary)
    request_date = Column(DateTime)

    def __repr__(self):
        return "<Request %r, %r>" % self.id, self.img, self.request_date


Base.metadata.create_all(engine)
