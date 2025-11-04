from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.database.session import Base
from app.domain.Enumeration.Enumeration import TipoCelular


class Telefone(Base):
    __tablename__ = "telefones"

    id = Column(Integer, primary_key=True, index=True)
    ddi = Column(Integer, nullable=True)  
    ddd = Column(Integer, nullable=True)
    numero = Column(String)
    tipo_linha = Column(Integer, nullable=False)  # 1 = celular, 2 = fixo
    tipo_uso = Column(Integer, nullable=False)    # 1 = pessoal, 2 = comercial
    pessoa_id = Column(Integer, ForeignKey("pessoas.id"))

    owner = relationship("Pessoa", back_populates="telefones")