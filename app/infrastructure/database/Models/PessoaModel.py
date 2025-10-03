from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.database.session import Base


class Pessoa(Base):
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    sobrenome = Column(String, index=True)
    cpf = Column(String, unique=True, index=True)
    usuario_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("Usuario", back_populates="pessoas")
    # Relacionamentos com outros modelos
    enderecos = relationship("Endereco", back_populates="owner", cascade="all, delete-orphan")
    telefones = relationship("Telefone", back_populates="owner", cascade="all, delete-orphan")