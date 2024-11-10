from sqlalchemy import Column, Integer, String, TIMESTAMP
from database import Base


class Item(Base):
    __tablename__ = "Posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    createdAt = Column(TIMESTAMP)
    updatedAt = Column(TIMESTAMP)

    @staticmethod
    def sdasd():
        pass
