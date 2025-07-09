from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .session import Base


class Endereco(Base):
    __tablename__ = "enderecos"

    id = Column(Integer, primary_key=True, index=True)
    rua = Column(String, index=True)
    numero = Column(String)
    complemento = Column(String, nullable=True)
    cidade = Column(String)
    estado = Column(String)
    cep = Column(String)
    pessoa_id = Column(Integer, ForeignKey("pessoas.id"))

    owner = relationship("Pessoa", back_populates="enderecos")