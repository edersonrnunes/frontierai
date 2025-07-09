from fastapi import APIRouter, Depends, status

from ..application import (EnderecoDtos, EnderecoUseCases, ItemDtos,
                           ItemUseCases, PessoaDtos, PessoaUseCases)
from ..domain import (EnderecoRepositories, ItemRepositories,
                      PessoaRepositories)
from .dependencies import (get_endereco_repository, get_item_repository,
                           get_pessoa_repository)

router = APIRouter()

@router.get("/")
def read_root():
    """
    Este endpoint retorna uma mensagem de boas-vindas.
    """
    return {"message": "Bem-vindo à Frontier AI!"}

@router.post("/items/", response_model=ItemDtos.Item, status_code=status.HTTP_201_CREATED, tags=["Items"])
def create_item(
    item_dto: ItemDtos.ItemCreate,
    repo: ItemRepositories = Depends(get_item_repository)
):
    uc = ItemUseCases.CreateItemUseCase(repo)
    result = uc.execute(item_dto)
    return result

@router.get("/items/", response_model=list[ItemDtos.Item], tags=["Items"])
def read_items(
    skip: int = 0, limit: int = 100,
    repo: ItemRepositories = Depends(get_item_repository)
):
    uc = ItemUseCases.ListItemsUseCase(repo)
    items = uc.execute(skip=skip, limit=limit)
    return items

## Pessoa
@router.post("/pessoas/", response_model=PessoaDtos.Pessoa, status_code=status.HTTP_201_CREATED, tags=["Pessoas"])
def create_pessoa(
    pessoa_dto: PessoaDtos.PessoaCreate,
    repo: PessoaRepositories = Depends(get_pessoa_repository)
):
    puc = PessoaUseCases.CreatePessoa(repo)
    result = puc.execute(pessoa_dto)
    return result

@router.get("/pessoas/", response_model=list[PessoaDtos.Pessoa], tags=["Pessoas"])
def read_pessoas(
    skip: int = 0, limit: int = 100,
    repo: PessoaRepositories = Depends(get_pessoa_repository)
):
    puc = PessoaUseCases.ListPessoa(repo)
    pessoas = puc.execute(skip=skip, limit=limit)
    return pessoas

@router.delete("/pessoas/{pessoa_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Pessoas"])
def delete_pessoa(
    pessoa_id: int,
    repo: PessoaRepositories.PessoaRepository = Depends(get_pessoa_repository)
):
    puc = PessoaUseCases.DeletePessoa(repo)
    puc.execute(pessoa_id=pessoa_id)
    return

## Endereço
@router.post("/pessoas/{pessoa_id}/enderecos/", response_model=EnderecoDtos.Endereco, status_code=status.HTTP_201_CREATED, tags=["Endereços"])
def create_endereco_for_pessoa(
    pessoa_id: int,
    endereco_dto: EnderecoDtos.EnderecoCreate,
    endereco_repo: EnderecoRepositories.EnderecoRepository = Depends(get_endereco_repository),
    pessoa_repo: PessoaRepositories.PessoaRepository = Depends(get_pessoa_repository)
):
    uc = EnderecoUseCases.CreateEndereco(endereco_repo, pessoa_repo)
    return uc.execute(pessoa_id=pessoa_id, endereco_create=endereco_dto)

@router.get("/pessoas/{pessoa_id}/enderecos/", response_model=list[EnderecoDtos.Endereco], tags=["Endereços"])
def read_enderecos_for_pessoa(
    pessoa_id: int,
    skip: int = 0, limit: int = 100,
    repo: EnderecoRepositories.EnderecoRepository = Depends(get_endereco_repository)
):
    uc = EnderecoUseCases.ListEnderecos(repo)
    return uc.execute(pessoa_id=pessoa_id, skip=skip, limit=limit)

@router.put("/enderecos/{endereco_id}", response_model=EnderecoDtos.Endereco, tags=["Endereços"])
def update_endereco(
    endereco_id: int,
    endereco_dto: EnderecoDtos.EnderecoCreate,
    repo: EnderecoRepositories.EnderecoRepository = Depends(get_endereco_repository)
):
    uc = EnderecoUseCases.UpdateEndereco(repo)
    return uc.execute(endereco_id=endereco_id, endereco_update=endereco_dto)

@router.delete("/enderecos/{endereco_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Endereços"])
def delete_endereco(
    endereco_id: int,
    repo: EnderecoRepositories.EnderecoRepository = Depends(get_endereco_repository)
):
    uc = EnderecoUseCases.DeleteEndereco(repo)
    uc.execute(endereco_id=endereco_id)
    return