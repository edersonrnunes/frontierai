from fastapi import HTTPException, status

from app.application.Dto import PessoaDtos
from app.domain.Repositories import PessoaRepositories, UserRepositories
from app.domain.Entities import PessoaEntities


class CreatePessoaUsuario:
    def __init__(self, pessoa_repo: PessoaRepositories.PessoaRepository, usuario_repo: UserRepositories.UserRepository):
        self._pessoa_repo = pessoa_repo
        self._usuario_repo = usuario_repo

    def execute(self, usuario_id: int, pessoa_create: PessoaDtos.PessoaCreate) -> PessoaEntities.Pessoa:
        usuario = self._usuario_repo.get_by_id(usuario_id)
        if not usuario:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuario com id {usuario_id} não encontrada")

        pessoa_entity = PessoaEntities.Pessoa(
            id=None,
            usuario_id=usuario_id,
            **pessoa_create.model_dump()
        )
        return self._pessoa_repo.add(pessoa_entity)


class CreatePessoa:
    def __init__(self, pessoa_repo: PessoaRepositories.PessoaRepository):
        self._repo = pessoa_repo

    def execute(self, pessoa_create: PessoaDtos.PessoaCreate) -> PessoaEntities.Pessoa:
        pessoa_entity = PessoaEntities.Pessoa(
            id=None,
            nome_completo=pessoa_create.nome_completo,
            cpf=pessoa_create.cpf,
            data_nascimento=pessoa_create.data_nascimento,
        )
        return self._repo.add(pessoa_entity)

class GetPessoaById:
    def __init__(self, pessoa_repo: PessoaRepositories.PessoaRepository):
        self._repo = pessoa_repo
    """Caso de uso para obter uma pessoa pelo ID."""
    def execute(self, pessoa_id: int) -> PessoaDtos.Pessoa:
        existing_pessoa = self._repo.get_by_id(pessoa_id)
        if not existing_pessoa:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Pessoa com id {pessoa_id} não encontrada")
        return existing_pessoa

       
class ListPessoa:
    def __init__(self, pessoa_repo: PessoaRepositories.PessoaRepository):
        self._repo = pessoa_repo

    def execute(self, skip: int = 0, limit: int = 100) -> list[PessoaEntities.Pessoa]:
        return self._repo.list(skip=skip, limit=limit)


class UpdatePessoa:
    def __init__(self, pessoa_repo: PessoaRepositories.PessoaRepository):
        self._repo = pessoa_repo

    def execute(self, pessoa_id: int, pessoa_update: PessoaDtos.PessoaBase) -> PessoaEntities.Pessoa:
        existing_pessoa = self._repo.get_by_id(pessoa_id)
        if not existing_pessoa:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Pessoa com id {pessoa_id} não encontrada")

        update_data = pessoa_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(existing_pessoa, key, value)

        return self._repo.update(existing_pessoa)


class DeletePessoa:
    def __init__(self, pessoa_repo: PessoaRepositories.PessoaRepository):
        self._repo = pessoa_repo

    def execute(self, pessoa_id: int) -> None:
        pessoa = self._repo.get_by_id(pessoa_id)
        if not pessoa:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Pessoa com id {pessoa_id} não encontrada")
        return self._repo.delete(pessoa_id=pessoa_id)
