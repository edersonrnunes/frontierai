from fastapi import Depends
from sqlalchemy.orm import Session

from ..infrastructure.database.session import SessionLocal
from ..infrastructure.database.EnderecoRepositories import \
    SQLAlchemyEnderecoRepository
from ..infrastructure.database.ItemRepositories import SQLAlchemyItemRepository
from ..infrastructure.database.PessoaRepositories import SQLAlchemyPessoaRepository
from ..domain.EnderecoRepositories import EnderecoRepository
from ..domain.ItemRepositories import ItemRepository
from ..domain.PessoaRepositories import PessoaRepository

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_item_repository(db: Session = Depends(get_db)) -> ItemRepository:
    return SQLAlchemyItemRepository(db_session=db)

def get_pessoa_repository(db: Session = Depends(get_db)) -> PessoaRepository:
    return SQLAlchemyPessoaRepository(db_session=db)

def get_endereco_repository(db: Session = Depends(get_db)) -> EnderecoRepository:
    return SQLAlchemyEnderecoRepository(db_session=db)
