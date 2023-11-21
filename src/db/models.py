from sqlalchemy import Column, String, Integer, Boolean
from .loader import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    username = Column(String, nullable=True)


class Parametrs(Base):
    __tablename__ = "params"

    user_id = Column(Integer, primary_key=True)
    weight = Column(Integer)
    height = Column(Integer)
    goal = Column(Boolean)