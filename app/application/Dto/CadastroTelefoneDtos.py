from pydantic import BaseModel, ConfigDict
from app.domain.Enumeration.Enumeration import TipoLinha, TipoUso



# Schema base para o Telefone, com os campos comuns.
class CadastroTelefoneBase(BaseModel):
    ddi: int | None = None
    ddd: int | None = None
    numero: str
    tipo_linha: TipoLinha   # 1 = celular, 2 = fixo, 3 = whatsapp
    tipo_uso: TipoUso     # 1 = pessoal, 2 = comercial
    

# Schema usado para criar um Telefone.
class CadastroTelefoneCreate(CadastroTelefoneBase):
    pass


# Schema usado para ler um Telefone do DB (inclui o ID e o ID da pessoa).
class Telefone(CadastroTelefoneBase):
    id: int
    pessoa_id: int

    model_config = ConfigDict(from_attributes=True)
