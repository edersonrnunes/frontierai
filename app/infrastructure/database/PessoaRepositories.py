from sqlalchemy.orm import Session
from ...domain import PessoaEntities as entities
from ...domain.PessoaRepositories import PessoaRepository
from . import PessoaModel as model

def _to_entity(db_pessoa: model.Pessoa) -> entities.Pessoa:
    """Mapeia o modelo SQLAlchemy para a entidade de domínio."""
    return entities.Pessoa(
        id=db_pessoa.id,
        nome=db_pessoa.nome,
        sobrenome=db_pessoa.sobrenome,
        cpf=db_pessoa.cpf
    )

class SQLAlchemyPessoaRepository(PessoaRepository):
    def __init__(self, db_session: Session):
        self._db = db_session

    def add(self, pessoa: entities.Pessoa) -> entities.Pessoa:
        db_pessoa = model.Pessoa(nome=pessoa.nome, sobrenome=pessoa.sobrenome, cpf=pessoa.cpf)
        self._db.add(db_pessoa)
        self._db.commit()
        self._db.refresh(db_pessoa)
        return _to_entity(db_pessoa)

    def get_by_id(self, pessoa_id: int) -> entities.Pessoa | None:
        pessoa_item = self._db.query(model.Pessoa).filter(model.Pessoa.id == pessoa_id).first()
        return _to_entity(pessoa_item) if pessoa_item else None

    def list(self, skip: int = 0, limit: int = 100) -> list[entities.Pessoa]:
        db_items = self._db.query(model.Pessoa).offset(skip).limit(limit).all()
        return [_to_entity(item) for item in db_items]

    def delete(self, pessoa_id: int) -> None:
        db_pessoa = self._db.query(model.Pessoa).filter(model.Pessoa.id == pessoa_id).first()
        if db_pessoa:
            self._db.delete(db_pessoa)
            self._db.commit()
    
    def update(self, pessoa: entities.Pessoa) -> entities.Pessoa:
        db_pessoa = self._db.query(model.Pessoa).filter(model.Pessoa.id == pessoa.id).first()
        if db_pessoa:
            db_pessoa.nome = pessoa.nome
            db_pessoa.sobrenome = pessoa.sobrenome
            db_pessoa.cpf = pessoa.cpf
            self._db.commit()
            self._db.refresh(db_pessoa)
            return _to_entity(db_pessoa)
        else:
            raise ValueError(f"Item with id {pessoa.id} not found.")
        