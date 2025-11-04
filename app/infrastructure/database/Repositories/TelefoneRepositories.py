from typing import List
from sqlalchemy.orm import session

from app.domain.Entities import TelefoneEntities as entities
from app.domain.Repositories.TelefoneRepositories import TelefoneRepository
from app.infrastructure.database.Models import TelefoneModel as model


def _to_entity(db_telefone: model.Telefone) -> entities.Telefone:
    """Mapeia o modelo SQLAlchemy para a entidade de domínio."""
    return entities.Telefone(
        id=db_telefone.id,
        ddi=db_telefone.ddi,
        ddd=db_telefone.ddd,
        numero=db_telefone.numero,
        tipo_linha=db_telefone.tipo_linha,
        tipo_uso=db_telefone.tipo_uso,
        pessoa_id=db_telefone.pessoa_id,
    )


class SQLAlchemyTelefoneRepository(TelefoneRepository):
    def __init__(self, db_session: session):
        self._db = db_session


    def add(self, telefone: entities.Telefone) -> entities.Telefone:
        db_telefone = model.Telefone(**telefone.__dict__)
        self._db.add(db_telefone)
        self._db.commit()
        self._db.refresh(db_telefone)
        return _to_entity(db_telefone)


    def get_by_id(self, telefone_id: int) -> entities.Telefone | None:
        db_telefone = self._db.query(model.Telefone).filter(model.Telefone.id == telefone_id).first()
        return _to_entity(db_telefone) if db_telefone else None


    def list_by_pessoa_id(self, pessoa_id: int, skip: int = 0, limit: int = 100) -> List[entities.Telefone]:
        db_telefones = (
            self._db.query(model.Telefone)
            .filter(model.Telefone.pessoa_id == pessoa_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
        return [_to_entity(e) for e in db_telefones]


    def update(self, telefone: entities.Telefone) -> entities.Telefone:
        db_telefone = self._db.query(model.Telefone).filter(model.Telefone.id == telefone.id).first()
        if db_telefone:
            for key, value in telefone.__dict__.items():
                setattr(db_telefone, key, value)
            self._db.commit()
            self._db.refresh(db_telefone)
            return _to_entity(db_telefone)
        return None  # Deve ser tratado pelo caso de uso


    def delete(self, telefone_id: int) -> None:
        db_telefone = self._db.query(model.Telefone).filter(model.Telefone.id == telefone_id).first()
        if db_telefone:
            self._db.delete(db_telefone)
            self._db.commit()