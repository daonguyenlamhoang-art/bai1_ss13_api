from pydantic import BaseModel, Field
from typing import Literal


class MenuItemCreate(BaseModel):
    dish_code: str = Field(..., min_length=1)
    dish_name: str = Field(..., min_length=1)
    calorie_count: int = Field(..., gt=0)
    price: float = Field(..., gt=0)
    status: Literal["AVAILABLE", "OUT_OF_STOCK"] = "AVAILABLE"

class MenuItemUpdate(BaseModel):
    dish_code: str 
    None = Field(None, min_length=1)
    dish_name: str 
    None = Field(None, min_length=1)
    calorie_count: int 
    None = Field(None, gt=0)
    price: float 
    None = Field(None, gt=0)
    status: Literal["AVAILABLE", "OUT_OF_STOCK"] 
    None = None


class MenuItemResponse(BaseModel):
    id: int
    dish_code: str
    dish_name: str
    calorie_count: int
    price: float
    status: str

    class Config:
        from_attributes = True