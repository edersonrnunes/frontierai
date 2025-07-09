from pydantic import BaseModel, ConfigDict

# Schema base para o Item, com os campos comuns.
class PessoaBase(BaseModel):
    nome: str
    sobrenome: str | None = None
    cpf: str

# Schema usado para criar um Item (não precisa de ID, pois é gerado pelo DB).
class PessoaCreate(PessoaBase):
    pass

# Schema usado para ler um Item do DB (inclui o ID).
class Pessoa(PessoaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)  # Permite que o Pydantic leia dados de modelos ORM e dataclasses.
