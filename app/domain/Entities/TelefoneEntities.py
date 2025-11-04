from dataclasses import dataclass
import app.domain.Enumeration.Enumeration as TipoCelular

@dataclass
class Telefone:
    id: int | None
    ddi: int | None
    ddd: int | None
    numero: str | None
    tipo_linha: int   # 1 = celular, 2 = fixo
    tipo_uso: int     # 1 = pessoal, 2 = comercial
    pessoa_id: int
