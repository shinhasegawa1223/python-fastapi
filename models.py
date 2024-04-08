from datetime import datetime
from sqlalchemy import Column, Integer, String, Enum, DateTime
from database import Base
from schemas import ItemStatus

# Item ClassがSQLAlchemyのモデルとなる
# DBの設計書みたいな感じのイメージ
class Item(Base):
    __tablename__ = "items"

    # pk , nullable not null
    id = Column(Integer, primary_key= True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description= Column(String, nullable=True)
    status = Column(Enum(ItemStatus), nullable=False, default=ItemStatus.ON_SALE)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    # onupdate 更新のたびに塗り替え