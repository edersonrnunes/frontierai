from sqlalchemy.orm import session
from app.domain.Entities import PessoaEntities as entities
from app.domain.Repositories.PessoaRepositories import PessoaRepository
from app.infrastructure.database.Models import PessoaModel as model


def _to_entity(db_pessoa: model.Pessoa) -> entities.Pessoa:
    """Mapeia o modelo SQLAlchemy para a entidade de domínio."""
    return entities.Pessoa(
        id=db_pessoa.id,
        nome_completo=db_pessoa.nome_completo,
        cpf=db_pessoa.cpf,
        data_nascimento=db_pessoa.data_nascimento,
        usuario_id=db_pessoa.usuario_id
    )


class SQLAlchemyPessoaRepository(PessoaRepository):
    def __init__(self, db_session: session):
        self._db = db_session


    def add(self, pessoa: entities.Pessoa) -> entities.Pessoa:
        db_pessoa = model.Pessoa(**pessoa.__dict__)
        self._db.add(db_pessoa)
        self._db.commit()
        self._db.refresh(db_pessoa)
        return _to_entity(db_pessoa)


    def get_by_id(self, pessoa_id: int) -> entities.Pessoa | None:
        pessoa_item = self._db.query(model.Pessoa).filter(model.Pessoa.id == pessoa_id).first()
        return _to_entity(pessoa_item) if pessoa_item else None
    
    def get_by_user_id(self, usuario_id: int) -> entities.Pessoa | None:
        # Busca uma pessoa associada a um usuário específico (via usuario_id).
        db_pessoa = self._db.query(model.Pessoa).filter(model.Pessoa.usuario_id == usuario_id).first()
        # Se encontrou a pessoa, converte o modelo do banco (SQLAlchemy) para entidade de domínio
        return _to_entity(db_pessoa) if db_pessoa else None



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
            db_pessoa.nome_completo = pessoa.nome_completo
            db_pessoa.cpf = pessoa.cpf
            db_pessoa.data_nascimento = pessoa.data_nascimento
            db_pessoa.usuario_id = pessoa.usuario_id
            self._db.commit()
            self._db.refresh(db_pessoa)
            return _to_entity(db_pessoa)
        else:
            raise ValueError(f"Item with id {pessoa.id} not found.")
        