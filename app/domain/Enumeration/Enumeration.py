from enum import Enum


class TipoEmpresa(Enum):
    COMERCIAL = "comercial"
    RESIDENCIAL = "residencial"


class TipoCelular(Enum):
    CELULAR = "celular"
    FIXO = "fixo"
    WHATSAPP = "whatsapp"