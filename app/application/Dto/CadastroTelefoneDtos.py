from pydantic import BaseModel, ConfigDict


# Schema base para o Telefone, com os campos comuns.
class CadastroTelefoneBase(BaseModel):
    numero: str
    tipo: str
    

# Schema usado para criar um Telefone.
class CadastroTelefoneCreate(CadastroTelefoneBase):
    pass


# Schema usado para ler um Telefone do DB (inclui o ID e o ID da pessoa).
class Telefone(CadastroTelefoneBase):
    id: int
    pessoa_id: int

    model_config = ConfigDict(from_attributes=True)
