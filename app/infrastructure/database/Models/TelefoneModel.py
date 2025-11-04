from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.infrastructure.database.session import Base
from app.domain.Enumeration.Enumeration import TipoLinha, TipoUso


class Telefone(Base):
    __tablename__ = "telefones"

    id = Column(Integer, primary_key=True, index=True)
    ddi = Column(Integer, nullable=True)  
    ddd = Column(Integer, nullable=True)
    numero = Column(String)
    tipo_linha = Column(Enum(TipoLinha), nullable=False) # 1 = celular, 2 = fixo, 3 = whatsapp
    tipo_uso = Column(Enum(TipoUso), nullable=False)# 1 = pessoal, 2 = comercial
    pessoa_id = Column(Integer, ForeignKey("pessoas.id"))

    owner = relationship("Pessoa", back_populates="telefones")