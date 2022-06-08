from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

from database import engine

Base = declarative_base()


class Response(Base):
    __tablename__ = "response"

    id = Column(Integer, primary_key=True, autoincrement=True)
    response_date = Column(DateTime)

    def __repr__(self):
        return "<Response %r, %r>" % self.id, self.request_date


Base.metadata.create_all(engine)
