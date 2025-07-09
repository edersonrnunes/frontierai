from sqlalchemy.orm import Session
from ...domain import ItemEntities as entities
from ...domain.ItemRepositories import ItemRepository
from . import ItemModels as model

def _to_entity(db_item: model.Item) -> entities.Item:
    """Mapeia o modelo SQLAlchemy para a entidade de domínio."""
    return entities.Item(
        id=db_item.id,
        name=db_item.name,
        description=db_item.description
    )

class SQLAlchemyItemRepository(ItemRepository):
    def __init__(self, db_session: Session):
        self._db = db_session

    def add(self, item: entities.Item) -> entities.Item:
        db_item = model.Item(name=item.name, description=item.description)
        self._db.add(db_item)
        self._db.commit()
        self._db.refresh(db_item)
        return _to_entity(db_item)

    def get_by_id(self, item_id: int) -> entities.Item | None:
        db_item = self._db.query(model.Item).filter(model.Item.id == item_id).first()
        return _to_entity(db_item) if db_item else None

    def list(self, skip: int = 0, limit: int = 100) -> list[entities.Item]:
        db_items = self._db.query(model.Item).offset(skip).limit(limit).all()
        return [_to_entity(item) for item in db_items]

    def delete(self, item_id: int) -> None:
        db_item = self._db.query(model.Item).filter(model.Item.id == item_id).first()
        if db_item:
            self._db.delete(db_item)
            self._db.commit()
    
    def update(self, item: entities.Item) -> entities.Item:
        db_item = self._db.query(model.Item).filter(model.Item.id == item.id).first()
        if db_item:
            db_item.name = item.name
            db_item.description = item.description
            self._db.commit()
            self._db.refresh(db_item)
            return _to_entity(db_item)
        else:
            raise ValueError(f"Item with id {item.id} not found.")
        