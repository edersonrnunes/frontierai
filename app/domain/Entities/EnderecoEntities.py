from dataclasses import dataclass


@dataclass
class Endereco:
    id: int | None
    rua: str
    bairro: str
    numero: str | None
    complemento: str | None
    cidade: str
    estado: str
    cep: str
    tipo: str
    pessoa_id: int