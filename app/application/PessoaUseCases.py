from fastapi import HTTPException, status
from ..domain import PessoaRepositories, PessoaEntities as entities
from . import PessoaDtos as PessoaDtos

class CreatePessoa:
    def __init__(self, pessoa_repo: PessoaRepositories.PessoaRepository):
        self._repo = pessoa_repo

    def execute(self, pessoa_create: PessoaDtos.PessoaCreate) -> entities.Pessoa:
        pessoa_entity = entities.Pessoa(
            id=None,
            nome=pessoa_create.nome,
            sobrenome=pessoa_create.sobrenome,
            cpf=pessoa_create.cpf
        )
        return self._repo.add(pessoa_entity)

class ListPessoa:
    def __init__(self, pessoa_repo: PessoaRepositories.PessoaRepository):
        self._repo = pessoa_repo

    def execute(self, skip: int = 0, limit: int = 100) -> list[entities.Pessoa]:
        return self._repo.list(skip=skip, limit=limit)

class DeletePessoa:
    def __init__(self, pessoa_repo: PessoaRepositories.PessoaRepository):
        self._repo = pessoa_repo

    def execute(self, pessoa_id: int) -> None:
        pessoa = self._repo.get_by_id(pessoa_id)
        if not pessoa:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Pessoa com id {pessoa_id} não encontrada")
        return self._repo.delete(pessoa_id=pessoa_id)