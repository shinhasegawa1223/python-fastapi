from enum import Enum
from typing import Optional
from schemas import ItemCreate

class ItemStatus(Enum):
    ON_SALE = "ON_SALE"
    SOLD_OUT = "SOLD_OUT"

class Item:
    def __init__(
            self,
            id: int,
            name:str,
            price: int,
            descripton: Optional[str],
            status: ItemStatus
    ):
        self.id = id
        self.name = name
        self.price = price
        self.descripton = descripton,
        self.status = status

items = [
    Item(1, "PC", 10000, "new", ItemStatus.ON_SALE),
    Item(2, "note book", 300000, "old", ItemStatus.SOLD_OUT),
    Item(3, "mac book", 400000, "new", ItemStatus.ON_SALE)
]

def find_all():
        return items

def find_by_id(id: int):
    for item in items:
         if item.id == id:
              return item
    return None

def find_by_name(name: str):
    filtered_items = []

    for item in items:
         if name in item.name:
              filtered_items.append(item)
    return filtered_items

        
def create(item_create : ItemCreate):
     new_item = Item(
          len(items) + 1,
          item_create.name,
          item_create.price,
          item_create.description,
          ItemStatus.ON_SALE,
     )
     items.append(new_item)
     return new_item

def update(id: int, item_update:ItemCreate):
     for item in items:
        if item.id == id:
            item.name =item_update.get("name", item.name)
            item.price =item_update.get("price", item.price)
            item.descripton =item_update.get("description", item.descripton)
            item.status =item_update.get("status", item.status)
            return item
     return None

def delete(id: int):
     for i in range(len(items)):
          if items[i].id == id:
               delete_item = items.pop(i)
               return delete_item
     return None
     