from dataclasses import dataclass

@dataclass
class Endereco:
    id: int | None
    rua: str
    numero: str | None
    complemento: str | None
    cidade: str
    estado: str
    cep: str
    pessoa_id: int