from dataclasses import dataclass


@dataclass
class Pessoa:
    id: int | None
    nome: str
    sobrenome: str
    cpf: str
    usuario_id: int