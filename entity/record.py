from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from database import engine

Base = declarative_base()


class Record(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    stack_trace = Column(Text)
    id_request = Column(Text, ForeignKey("request.id"))
    id_response = Column(Integer, ForeignKey("response.id"))
    id_model = Column(Integer, ForeignKey("model.id"))

    def __repr__(self):
        return "<Logs %r, %r, %r, %r, %r>" % self.id, self.stack_trace, self.id_request, self.id_response, self.id_model


Base.metadata.create_all(engine)