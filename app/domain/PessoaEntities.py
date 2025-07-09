from dataclasses import dataclass

@dataclass
class Pessoa:
    id: int | None
    nome: str | None = None
    sobrenome: str | None = None
    cpf: str | None = None