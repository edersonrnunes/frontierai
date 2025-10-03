from fastapi import HTTPException, status

from app.application.Dto import CadastroTelefoneDtos
from app.domain.Entities import TelefoneEntities
from app.domain.Repositories import (
    PessoaRepositories,
    TelefoneRepositories
)


class CreateTelefone:
    def __init__(self, telefone_repo: TelefoneRepositories.TelefoneRepository, pessoa_repo: PessoaRepositories.PessoaRepository):
        self._telefone_repo = telefone_repo
        self._pessoa_repo = pessoa_repo

    def execute(self, pessoa_id: int, telefone_create: CadastroTelefoneDtos.CadastroTelefoneCreate) -> TelefoneEntities.Telefone:
        pessoa = self._pessoa_repo.get_by_id(pessoa_id)
        if not pessoa:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Pessoa com id {pessoa_id} não encontrada")

        telefone_entity = TelefoneEntities.Telefone(
            id=None,
            pessoa_id=pessoa_id,
            **telefone_create.model_dump()
        )
        return self._telefone_repo.add(telefone_entity)


class ListTelefones:
    def __init__(self, telefone_repo: TelefoneRepositories.TelefoneRepository):
        self._repo = telefone_repo

    def execute(self, pessoa_id: int, skip: int = 0, limit: int = 100) -> list[TelefoneEntities.Telefone]:
        return self._repo.list_by_pessoa_id(pessoa_id=pessoa_id, skip=skip, limit=limit)


class UpdateTelefone:
    def __init__(self, telefone_repo: TelefoneRepositories.TelefoneRepository):
        self._repo = telefone_repo

    def execute(self, telefone_id: int, telefone_update: CadastroTelefoneDtos.CadastroTelefoneCreate) -> TelefoneEntities.telefone:
        existing_telefone = self._repo.get_by_id(telefone_id)
        if not existing_telefone:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Endereço com id {telefone_id} não encontrado")

        update_data = telefone_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(existing_telefone, key, value)

        return self._repo.update(existing_telefone)

class DeleteTelefone:
    def __init__(self, telefone_repo: TelefoneRepositories.TelefoneRepository):
        self._repo = telefone_repo

    def execute(self, telefone_id: int) -> None:
        telefone = self._repo.get_by_id(telefone_id)
        if not telefone:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Endereço com id {telefone_id} não encontrado")
        self._repo.delete(telefone_id)
