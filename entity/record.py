from sqlalchemy import Column, Text, Integer, ForeignKey

from database import Base


class Record(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    stack_trace = Column(Text)
    id_request = Column(Text, ForeignKey("request.id"))
    id_response = Column(Integer, ForeignKey("response.id"))
    id_model = Column(Integer, ForeignKey("model.id"))

    def __repr__(self):
        return f"<Logs {self.id}, {self.id_response}, {self.id_request}, {self.id_model}, {self.stack_trace}>"
