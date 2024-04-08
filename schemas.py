from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel,Field, ConfigDict

# バリデーションの際に使用するクラス
# pydanticを使用する

class ItemStatus(Enum):
    ON_SALE = "ON_SALE"
    SOLD_OUT = "SOLD_OUT"

class ItemCreate(BaseModel):
    name: str = Field(min_length=2, max_length=20, examples=["PC"])
    price: int = Field(gt=0, examples=[10000]) 
    description: Optional[str] = Field( default=None, examples=["new"])


class ItemUpdate(BaseModel):
    name: Optional[str] =Field(None,min_length=2, max_length=20, examples=["PC"])
    price: Optional[int] = Field( default=None,gt=0, examples=[10000])
    description: Optional[str] = Field(default=None,examples=["new"])
    status: Optional[ItemStatus] = Field(default=None, examples=[ItemStatus.ON_SALE])

class ItemResponse(BaseModel):
    id: int = Field(gt=0, examples=[1])
    name: str = Field(min_length=2, max_length=20, examples=["PC"])
    price : int = Field(gt=0, examples=[10000])
    description: Optional[str] = Field(default=None, examples=["new"])
    status : ItemStatus = Field(examples=[ItemStatus.ON_SALE])
    created_at: datetime
    updated_at: datetime

    # response  このスキーマはormを自動的に受取　内部的に適切なバリデーション
    model_config = ConfigDict(from_attributes=True)