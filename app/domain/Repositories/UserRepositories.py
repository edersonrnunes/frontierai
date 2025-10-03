from abc import ABC, abstractmethod
from typing import List

from app.domain.Entities import UserEntities as entities


class UserRepository(ABC):
    """Interface abstrata para o repositório de usuários."""
    @abstractmethod
    def add(self, usuario: entities.Usuario) -> entities.Usuario:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, usuario_id: int) -> entities.Usuario | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_username(self, username: str) -> entities.Usuario | None:
        """Busca um usuário pelo nome de usuário."""
        raise NotImplementedError