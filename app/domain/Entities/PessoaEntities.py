from dataclasses import dataclass
from datetime import date


@dataclass
class Pessoa:
    id: int | None
    nome_completo: str
    cpf: str
    usuario_id: int
    data_nascimento: date | None = None