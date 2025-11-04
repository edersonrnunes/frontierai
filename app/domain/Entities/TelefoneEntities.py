from dataclasses import dataclass
from app.domain.Enumeration.Enumeration import TipoLinha, TipoUso

@dataclass
class Telefone:
    id: int | None
    ddi: int | None
    ddd: int | None
    numero: str | None
    tipo_linha: TipoLinha   # 1 = celular, 2 = fixo, 3 = whatsapp
    tipo_uso: TipoUso     # 1 = pessoal, 2 = comercial
    pessoa_id: int
