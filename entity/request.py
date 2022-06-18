from sqlalchemy import Column, Text, DateTime

from database import Base


class Request(Base):
    __tablename__ = "request"

    id = Column(Text, primary_key=True)
    img_path = Column(Text)
    request_date = Column(DateTime)

    def __repr__(self):
        return f"<Request {self.img_path}, {self.request_date}"
