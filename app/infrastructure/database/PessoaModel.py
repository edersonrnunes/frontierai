from sqlalchemy import Column, Integer, String
from .session import Base

class Pessoa(Base):
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    sobrenome = Column(String, index=True)
    cpf = Column(String, unique=True, index=True)
