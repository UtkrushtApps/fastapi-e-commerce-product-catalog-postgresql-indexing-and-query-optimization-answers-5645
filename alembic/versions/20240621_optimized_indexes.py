"""
Revision ID: 20240621_optimized_indexes
Revises: <previous_revision_id>
Create Date: 2024-06-21 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Drop old slow/unused indexes if any (examples, adapt as needed)
    # op.drop_index('ix_products_category_id', table_name='products')

    # Add efficient composite index for product filtering
    op.create_index(
        'ix_products_category_brand',
        'products',
        ['category_id', 'brand_id']
    )

    # Optional: add index on price for sorting (if not present)
    # op.create_index('ix_products_price', 'products', ['price'])

def downgrade():
    op.drop_index('ix_products_category_brand', table_name='products')
    # op.drop_index('ix_products_price', table_name='products')
