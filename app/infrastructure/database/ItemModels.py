from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Text, Float, BigInteger
from .session import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

