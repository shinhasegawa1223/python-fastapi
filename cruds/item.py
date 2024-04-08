from typing import Optional
from schemas import ItemCreate,ItemStatus, ItemUpdate


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

# def update(id: int, item_update:ItemUpdate):
#      for item in items:
#         if item.id == id:
#             item.name =item.name if item_update.name is None else item_update.name
#             item.price ==item.price if item_update.price is None else item_update.price
#             item.descripton =item.descripton if item_update.description is None else item_update.description
#             item.status =item.status if item_update.status is None else item_update.status
#             return item
#      return None

def update(id: int, item_update: ItemUpdate):
    """
    指定されたIDのアイテムを更新します。

    :param id: 更新対象のアイテムID
    :param item_update: 更新情報を含むItemUpdateオブジェクト
    :return: 更新されたアイテム、またはNone（IDが見つからなかった場合）
    """
    for item in items:
        if item.id == id:
            if item_update.name is not None:
                item.name = item_update.name
            if item_update.price is not None:
                item.price = item_update.price
            if item_update.description is not None:
                item.description = item_update.description
            if item_update.status is not None:
                item.status = item_update.status
            return item
    return None

def delete(id: int):
     for i in range(len(items)):
          if items[i].id == id:
               delete_item = items.pop(i)
               return delete_item
     return None
     