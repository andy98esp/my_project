import application.db as db

from sqlalchemy import create_engine, Column, Integer, Float, String, MetaData


class Product(db.Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    price = Column(Float, nullable=True)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'Product({self.name}, {self.price})'

    def __str__(self):
        return self.name
