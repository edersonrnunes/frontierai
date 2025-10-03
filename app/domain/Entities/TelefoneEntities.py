from dataclasses import dataclass
import app.domain.Enumeration.Enumeration as TipoCelular

@dataclass
class Telefone:
    id: int | None
    numero: str | None
    tipo: TipoCelular
    pessoa_id: int
