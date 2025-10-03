from typing import List
from sqlalchemy.orm import session

from app.domain.Entities import EnderecoEntities as entities
from app.domain.Repositories.EnderecoRepositories import EnderecoRepository
from app.infrastructure.database.Models import EnderecoModel as model


def _to_entity(db_endereco: model.Endereco) -> entities.Endereco:
    """Mapeia o modelo SQLAlchemy para a entidade de domínio."""
    return entities.Endereco(
        id=db_endereco.id,
        rua=db_endereco.rua,
        bairro=db_endereco.bairro,
        numero=db_endereco.numero,
        complemento=db_endereco.complemento,
        cidade=db_endereco.cidade,
        estado=db_endereco.estado,
        cep=db_endereco.cep,
        tipo=db_endereco.tipo,
        pessoa_id=db_endereco.pessoa_id,
    )


class SQLAlchemyEnderecoRepository(EnderecoRepository):
    def __init__(self, db_session: session):
        self._db = db_session


    def add(self, endereco: entities.Endereco) -> entities.Endereco:
        db_endereco = model.Endereco(**endereco.__dict__)
        self._db.add(db_endereco)
        self._db.commit()
        self._db.refresh(db_endereco)
        return _to_entity(db_endereco)


    def get_by_id(self, endereco_id: int) -> entities.Endereco | None:
        db_endereco = self._db.query(model.Endereco).filter(model.Endereco.id == endereco_id).first()
        return _to_entity(db_endereco) if db_endereco else None


    def list_by_pessoa_id(self, pessoa_id: int, skip: int = 0, limit: int = 100) -> List[entities.Endereco]:
        db_enderecos = (
            self._db.query(model.Endereco)
            .filter(model.Endereco.pessoa_id == pessoa_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
        return [_to_entity(e) for e in db_enderecos]


    def update(self, endereco: entities.Endereco) -> entities.Endereco:
        db_endereco = self._db.query(model.Endereco).filter(model.Endereco.id == endereco.id).first()
        if db_endereco:
            for key, value in endereco.__dict__.items():
                setattr(db_endereco, key, value)
            self._db.commit()
            self._db.refresh(db_endereco)
            return _to_entity(db_endereco)
        return None  # Deve ser tratado pelo caso de uso


    def delete(self, endereco_id: int) -> None:
        db_endereco = self._db.query(model.Endereco).filter(model.Endereco.id == endereco_id).first()
        if db_endereco:
            self._db.delete(db_endereco)
            self._db.commit()