from ..domain import PessoaRepositories, PessoaEntities as entities
from . import PessoaDtos as PessoaDtos

class CreatePessoaUseCase:
    def __init__(self, pessoa_repo: PessoaRepositories):
        self._repo = pessoa_repo

    def execute(self, pessoa_create: PessoaDtos.PessoaCreate) -> entities.Pessoa:
        pessoa_entity = entities.Pessoa(
            id=None,
            nome=pessoa_create.nome,
            sobrenome=pessoa_create.sobrenome,
            cpf=pessoa_create.cpf
        )
        return self._repo.add(pessoa_entity)

class ListPessoaUseCase:
    def __init__(self, pessoa_repo: PessoaRepositories):
        self._repo = pessoa_repo

    def execute(self, skip: int = 0, limit: int = 100) -> list[entities.Pessoa]:
        return self._repo.list(skip=skip, limit=limit)
