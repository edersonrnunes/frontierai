from typing import List
from ..domain import entities, repositories

class InMemoryItemRepository(repositories.ItemRepository):
    _items: dict[int, entities.Item]
    _next_id: int

    def __init__(self):
        self._items = {}
        self._next_id = 1

    def add(self, item: entities.Item) -> entities.Item:
        item.id = self._next_id
        self._items[self._next_id] = item
        self._next_id += 1
        return item

    def list(self, skip: int = 0, limit: int = 100) -> List[entities.Item]:
        return list(self._items.values())[skip:skip+limit]
    
    def delete(self, item_id: int) -> None:
        raise NotImplementedError
    
    def update(self, item: entities.Item) -> entities.Item:
        item.id = item.id
        self._items[self._next_id] = item
        return item