from sqlalchemy import Column, Integer, Text

from database import Base


class Model(Base):
    __tablename__ = "model"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(Text)
    path = Column(Text)

    def __repr__(self):
        return f"<Model {self.id}, {self.name}, {self.path}>"
