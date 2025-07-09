from abc import ABC, abstractmethod
from typing import List

from . import EnderecoEntities as entities


class EnderecoRepository(ABC):
    @abstractmethod
    def add(self, endereco: entities.Endereco) -> entities.Endereco:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, endereco_id: int) -> entities.Endereco | None:
        raise NotImplementedError

    @abstractmethod
    def list_by_pessoa_id(self, pessoa_id: int, skip: int = 0, limit: int = 100) -> List[entities.Endereco]:
        raise NotImplementedError

    @abstractmethod
    def update(self, endereco: entities.Endereco) -> entities.Endereco:
        raise NotImplementedError

    @abstractmethod
    def delete(self, endereco_id: int) -> None:
        raise NotImplementedError