from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import get_products_filtered
from app.database import get_async_session
from app.models import Product
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter()

class ProductOut(BaseModel):
    id: int
    name: str
    category_id: int
    brand_id: int
    price: float
    stock: int

    class Config:
        orm_mode = True

@router.get("/products", response_model=List[ProductOut])
async def list_products(
    category_id: Optional[int] = Query(None),
    brand_id: Optional[int] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_async_session()),
):
    products = await get_products_filtered(db, category_id=category_id, brand_id=brand_id, skip=skip, limit=limit)
    return products
