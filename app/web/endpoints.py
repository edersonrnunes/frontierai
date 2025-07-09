from fastapi import APIRouter, Depends, status

from ..application import ItemDtos, ItemUseCases, PessoaDtos, PessoaUseCases
from ..domain import ItemRepositories, PessoaRepositories
from .dependencies import get_item_repository, get_pessoa_repository

router = APIRouter()

@router.get("/")
def read_root():
    """
    Este endpoint retorna uma mensagem de boas-vindas.
    """
    return {"message": "Bem-vindo à API com DDD!"}

@router.post("/items/", response_model=ItemDtos.Item, status_code=status.HTTP_201_CREATED)
def create_item(
    item_dto: ItemDtos.ItemCreate,
    repo: ItemRepositories = Depends(get_item_repository)
):
    uc = ItemUseCases.CreateItemUseCase(repo)
    result = uc.execute(item_dto)
    return result

@router.get("/items/", response_model=list[ItemDtos.Item])
def read_items(
    skip: int = 0, limit: int = 100,
    repo: ItemRepositories = Depends(get_item_repository)
):
    uc = ItemUseCases.ListItemsUseCase(repo)
    items = uc.execute(skip=skip, limit=limit)
    return items

## Pessoa
@router.post("/cadastro_pessoa/", response_model=PessoaDtos.Pessoa, status_code=status.HTTP_201_CREATED)
def create_pessoa(
    pessoa_dto: PessoaDtos.PessoaCreate,
    repo: PessoaRepositories = Depends(get_pessoa_repository)
):
    puc = PessoaUseCases.CreatePessoaUseCase(repo)
    result = puc.execute(pessoa_dto)
    return result

@router.get("/lista_pessoas/", response_model=list[PessoaDtos.Pessoa])
def read_pessoas(
    skip: int = 0, limit: int = 100,
    repo: PessoaRepositories = Depends(get_pessoa_repository)
):
    puc = PessoaUseCases.ListPessoaUseCase(repo)
    pessoas = puc.execute(skip=skip, limit=limit)
    return pessoas
