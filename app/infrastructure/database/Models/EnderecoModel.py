from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.database.session import Base
from app.domain.Enumeration.Enumeration import TipoEmpresa


class Endereco(Base):
    __tablename__ = "enderecos"

    id = Column(Integer, primary_key=True, index=True)
    rua = Column(String, index=True)
    bairro = Column(String, nullable=False)
    numero = Column(String)
    complemento = Column(String, nullable=True)
    cidade = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    cep = Column(String, nullable=False)
    tipo = Column(String, nullable=False, default=TipoEmpresa.COMERCIAL.value)
    pessoa_id = Column(Integer, ForeignKey("pessoas.id"))

    owner = relationship("Pessoa", back_populates="enderecos")