from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

from database import engine

Base = declarative_base()


class Model(Base):
    __tablename__ = "model"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(Text)
    path = Column(Text)

    def __repr__(self):
        return "<Model %r, %r, %r>" % self.id, self.name, self.path


Base.metadata.create_all(engine)
