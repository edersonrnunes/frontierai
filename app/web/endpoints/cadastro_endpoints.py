import logging
logger = logging.getLogger(__name__)

from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated

from app.application.UseCase import (
    PessoaUseCases,
    EnderecoUseCases,
    ItemUseCases
)

from app.application.Dto import (
    EnderecoDtos,
    ItemDtos,
    PessoaDtos
)

from app.domain.Entities import (
    UserEntities
)

from app.domain.Repositories import (
    PessoaRepositories,
    EnderecoRepositories,
    ItemRepositories,
    UserRepositories
)

from app.web.dependencies import (
    get_endereco_repository,
    get_item_repository,
    get_pessoa_repository,
    get_current_active_user,
    get_autenticacao_repository
)

router = APIRouter()

@router.get("/")
def read_root():
    """
    Este endpoint retorna uma mensagem de boas-vindas.
    """
    return {"message": "Bem-vindo à Frontier AI!"}

@router.get("/health", tags=["Health"])
def health_check(
    repo: PessoaRepositories.PessoaRepository = Depends(get_pessoa_repository)
):
    pessoa_use_cases = PessoaUseCases.GetPessoaById(repo)
    pessoa = pessoa_use_cases.execute(pessoa_id=1)
    if not pessoa:
        return {"status": "Database connection failed"}, status.HTTP_500_INTERNAL_SERVER_ERROR
    return {"status": "ok"}

## Item
@router.post("/items/", response_model=ItemDtos.Item, status_code=status.HTTP_201_CREATED, tags=["Items"])
def create_item(
    current_user: Annotated[UserEntities.Usuario, Depends(get_current_active_user)],
    item_dto: ItemDtos.ItemCreate,
    repo: ItemRepositories.ItemRepository = Depends(get_item_repository),
):
    print(f"User '{current_user.username}' creating item with data: {item_dto}")
    item_use_cases = ItemUseCases.CreateItemUseCase(repo)
    result = item_use_cases.execute(item_dto)
    return result

@router.get("/items/", response_model=list[ItemDtos.Item], tags=["Items"])
def read_items(
    current_user: Annotated[UserEntities.Usuario, Depends(get_current_active_user)],
    skip: int = 0, limit: int = 100,
    repo: ItemRepositories = Depends(get_item_repository)
):
    print(f"User '{current_user.username}' reading items with skip={skip} and limit={limit}")
    item_use_cases = ItemUseCases.ListItemsUseCase(repo)
    items = item_use_cases.execute(skip=skip, limit=limit)
    return items

@router.get("/items/color/{color}", response_model=list[ItemDtos.Item], tags=["Items"])
def read_items_by_color(
    current_user: Annotated[UserEntities.Usuario, Depends(get_current_active_user)],
    color: str,
    repo: ItemRepositories.ItemRepository = Depends(get_item_repository)
):
    print(f"User '{current_user.username}' reading items with color={color}")
    item_use_cases = ItemUseCases.GetItemsByColorUseCase(repo)
    items = item_use_cases.execute(color=color)
    return items


## Pessoa
@router.post("/usuario/{usuario_id}/pessoas/", response_model=PessoaDtos.Pessoa, status_code=status.HTTP_201_CREATED, tags=["Pessoas"])
def create_pessoa_for_usuario(
    usuario_id: int,
    pessoa_dto: PessoaDtos.PessoaCreate,
    usuario_repo: UserRepositories.UserRepository = Depends(get_autenticacao_repository),
    pessoa_repo: PessoaRepositories.PessoaRepository = Depends(get_pessoa_repository)
):
    print(f"Creating pessoa for usuario ID: {usuario_id} with data: {pessoa_dto}")
    pessoa_use_cases = PessoaUseCases.CreatePessoaUsuario(pessoa_repo, usuario_repo)
    return pessoa_use_cases.execute(usuario_id=usuario_id, pessoa_create=pessoa_dto)


@router.post("/pessoas/", response_model=PessoaDtos.PessoaBase, status_code=status.HTTP_201_CREATED, tags=["Pessoas"])
def create_pessoa(
    current_user: Annotated[UserEntities.Usuario, Depends(get_current_active_user)],
    pessoa_dto: PessoaDtos.PessoaCreate,
    repo: PessoaRepositories = Depends(get_pessoa_repository)
):
    """
    Endpoint protegido para obter informações do usuário logado.
    Requer um token JWT válido no header `Authorization: Bearer <token>`.
    """
    print(f"User '{current_user.username}' creating pessoa with data: {pessoa_dto}")
    pessoa_use_cases = PessoaUseCases.CreatePessoa(repo)
    result = pessoa_use_cases.execute(pessoa_dto)
    return result

@router.get("/pessoas/", response_model=list[PessoaDtos.Pessoa], tags=["Pessoas"])
def list_pessoas(
    current_user: Annotated[UserEntities.Usuario, Depends(get_current_active_user)],
    skip: int = 0, limit: int = 100,
    repo: PessoaRepositories = Depends(get_pessoa_repository)
):
    """
    Endpoint protegido para obter informações do usuário logado.
    Requer um token JWT válido no header `Authorization: Bearer <token>`.
    """
    print(f"User '{current_user.username}' reading pessoas with skip={skip} and limit={limit}")
    pessoa_use_cases = PessoaUseCases.ListPessoa(repo)
    pessoas = pessoa_use_cases.execute(skip=skip, limit=limit)
    return pessoas

@router.get("/pessoas/{pessoa_id}", response_model=PessoaDtos.PessoaBase, tags=["Pessoas"])
def get_pessoa_by_id(
    current_user: Annotated[UserEntities.Usuario, Depends(get_current_active_user)],
    pessoa_id: int,
    repo: PessoaRepositories.PessoaRepository = Depends(get_pessoa_repository)
):
    print(f"User '{current_user.username}' get pessoa with pesso_id")
    pessoa_use_cases = PessoaUseCases.GetPessoaById(repo)
    pessoa = pessoa_use_cases.execute(pessoa_id=pessoa_id)
    return pessoa


@router.put("/pessoas/{pessoa_id}", response_model=PessoaDtos.PessoaBase, tags=["Pessoas"])
def update_pessoa(
    pessoa_id: int,
    pessoa_dto: PessoaDtos.PessoaBase,
    repo: PessoaRepositories.PessoaRepository = Depends(get_pessoa_repository)
):
    print(f"Updating endereco with ID: {pessoa_id} with data: {pessoa_dto}")
    pessoa_use_cases = PessoaUseCases.UpdatePessoa(repo)
    return pessoa_use_cases.execute(pessoa_id=pessoa_id, pessoa_update=pessoa_dto)

@router.delete("/pessoas/{pessoa_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Pessoas"])
def delete_pessoa(
    pessoa_id: int,
    repo: PessoaRepositories.PessoaRepository = Depends(get_pessoa_repository)
):
    logger.info(f"Deleting pessoa with ID: {pessoa_id}")
    pessoa_use_cases = PessoaUseCases.DeletePessoa(repo)
    pessoa_use_cases.execute(pessoa_id=pessoa_id)
    return

## Endereço
@router.post("/pessoas/{pessoa_id}/enderecos/", response_model=EnderecoDtos.Endereco, status_code=status.HTTP_201_CREATED, tags=["Endereços"])
def create_endereco_for_pessoa(
    pessoa_id: int,
    endereco_dto: EnderecoDtos.EnderecoCreate,
    endereco_repo: EnderecoRepositories.EnderecoRepository = Depends(get_endereco_repository),
    pessoa_repo: PessoaRepositories.PessoaRepository = Depends(get_pessoa_repository)
):
    print(f"Creating endereco for pessoa ID: {pessoa_id} with data: {endereco_dto}")
    endereco_use_cases = EnderecoUseCases.CreateEndereco(endereco_repo, pessoa_repo)
    return endereco_use_cases.execute(pessoa_id=pessoa_id, endereco_create=endereco_dto)

@router.get("/pessoas/{pessoa_id}/enderecos/", response_model=list[EnderecoDtos.Endereco], tags=["Endereços"])
def read_enderecos_for_pessoa(
    pessoa_id: int,
    skip: int = 0, limit: int = 100,
    repo: EnderecoRepositories.EnderecoRepository = Depends(get_endereco_repository)
):
    print(f"Reading enderecos for pessoa ID: {pessoa_id} with skip={skip} and limit={limit}")
    endereco_use_cases = EnderecoUseCases.ListEnderecos(repo)
    return endereco_use_cases.execute(pessoa_id=pessoa_id, skip=skip, limit=limit)

@router.put("/enderecos/{endereco_id}", response_model=EnderecoDtos.Endereco, tags=["Endereços"])
def update_endereco(
    endereco_id: int,
    endereco_dto: EnderecoDtos.EnderecoCreate,
    repo: EnderecoRepositories.EnderecoRepository = Depends(get_endereco_repository)
):
    print(f"Updating endereco with ID: {endereco_id} with data: {endereco_dto}")
    endereco_use_cases = EnderecoUseCases.UpdateEndereco(repo)
    return endereco_use_cases.execute(endereco_id=endereco_id, endereco_update=endereco_dto)

@router.delete("/enderecos/{endereco_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Endereços"])
def delete_endereco(
    endereco_id: int,
    repo: EnderecoRepositories.EnderecoRepository = Depends(get_endereco_repository)
):
    print(f"Deleting endereco with ID: {endereco_id}")
    endereco_use_cases = EnderecoUseCases.DeleteEndereco(repo)
    endereco_use_cases.execute(endereco_id=endereco_id)
    return