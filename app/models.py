from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    products = relationship('Product', back_populates='category')

class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    products = relationship('Product', back_populates='brand')

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), index=True, nullable=False)
    brand_id = Column(Integer, ForeignKey('brands.id'), index=True, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    category = relationship('Category', back_populates='products')
    brand = relationship('Brand', back_populates='products')
