from pydantic import BaseModel, ConfigDict


# Schema base para o Endereço, com os campos comuns.
class EnderecoBase(BaseModel):
    rua: str
    bairro: str | None
    numero: str | None = None
    complemento: str | None = None
    cidade: str
    estado: str
    cep: str
    tipo: str

# Schema usado para criar um Endereço.
class EnderecoCreate(EnderecoBase):
    pass


# Schema usado para ler um Endereço do DB (inclui o ID e o ID da pessoa).
class Endereco(EnderecoBase):
    id: int
    pessoa_id: int

    model_config = ConfigDict(from_attributes=True)