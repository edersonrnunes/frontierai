from fastapi import HTTPException, status

from app.application.Dto import EnderecoDtos
from app.domain.Entities import EnderecoEntities
from app.domain.Repositories import (
    PessoaRepositories,
    EnderecoRepositories
)


class CreateEndereco:
    def __init__(self, endereco_repo: EnderecoRepositories.EnderecoRepository, pessoa_repo: PessoaRepositories.PessoaRepository):
        self._endereco_repo = endereco_repo
        self._pessoa_repo = pessoa_repo

    def execute(self, pessoa_id: int, endereco_create: EnderecoDtos.EnderecoCreate) -> EnderecoEntities.Endereco:
        pessoa = self._pessoa_repo.get_by_id(pessoa_id)
        if not pessoa:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Pessoa com id {pessoa_id} não encontrada")

        endereco_entity = EnderecoEntities.Endereco(
            id=None,
            pessoa_id=pessoa_id,
            **endereco_create.model_dump()
        )
        return self._endereco_repo.add(endereco_entity)


class ListEnderecos:
    def __init__(self, endereco_repo: EnderecoRepositories.EnderecoRepository):
        self._repo = endereco_repo

    def execute(self, pessoa_id: int, skip: int = 0, limit: int = 100) -> list[EnderecoEntities.Endereco]:
        return self._repo.list_by_pessoa_id(pessoa_id=pessoa_id, skip=skip, limit=limit)


class UpdateEndereco:
    def __init__(self, endereco_repo: EnderecoRepositories.EnderecoRepository):
        self._repo = endereco_repo

    def execute(self, endereco_id: int, endereco_update: EnderecoDtos.EnderecoCreate) -> EnderecoEntities.Endereco:
        existing_endereco = self._repo.get_by_id(endereco_id)
        if not existing_endereco:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Endereço com id {endereco_id} não encontrado")

        update_data = endereco_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(existing_endereco, key, value)

        return self._repo.update(existing_endereco)

class DeleteEndereco:
    def __init__(self, endereco_repo: EnderecoRepositories.EnderecoRepository):
        self._repo = endereco_repo

    def execute(self, endereco_id: int) -> None:
        endereco = self._repo.get_by_id(endereco_id)
        if not endereco:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Endereço com id {endereco_id} não encontrado")
        self._repo.delete(endereco_id)
