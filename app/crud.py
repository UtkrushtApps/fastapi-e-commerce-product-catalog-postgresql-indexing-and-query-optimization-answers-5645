from sqlalchemy.future import select
from sqlalchemy import and_  # for combining filter conditions
from app.models import Product
from sqlalchemy.ext.asyncio import AsyncSession

async def get_products_filtered(db: AsyncSession, category_id: int = None, brand_id: int = None, skip: int = 0, limit: int = 20):
    filters = []
    if category_id:
        filters.append(Product.category_id == category_id)
    if brand_id:
        filters.append(Product.brand_id == brand_id)
    stmt = select(Product)
    if filters:
        stmt = stmt.where(and_(*filters))
    stmt = stmt.offset(skip).limit(limit)
    result = await db.execute(stmt)
    products = result.scalars().all()
    return products
