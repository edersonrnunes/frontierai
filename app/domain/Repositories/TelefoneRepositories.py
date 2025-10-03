from abc import ABC, abstractmethod
from typing import List

from app.domain.Entities import TelefoneEntities as entities


class TelefoneRepository(ABC):
    @abstractmethod
    def add(self, telefone: entities.Telefone) -> entities.Telefone:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, telefone_id: int) -> entities.Telefone | None:
        raise NotImplementedError

    @abstractmethod
    def list_by_pessoa_id(self, pessoa_id: int, skip: int = 0, limit: int = 100) -> List[entities.Telefone]:
        raise NotImplementedError

    @abstractmethod
    def update(self, telefone: entities.Telefone) -> entities.Telefone:
        raise NotImplementedError

    @abstractmethod
    def delete(self, telefone_id: int) -> None:
        raise NotImplementedError
