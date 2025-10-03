from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.database.session import Base
from app.domain.Enumeration.Enumeration import TipoCelular


class Telefone(Base):
    __tablename__ = "telefones"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String)
    tipo = Column(String, nullable=False, default=TipoCelular.CELULAR.value)
    pessoa_id = Column(Integer, ForeignKey("pessoas.id"))

    owner = relationship("Pessoa", back_populates="telefones")