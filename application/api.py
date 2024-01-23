from application import init_sentry
init_sentry()

from enum import Enum

from fastapi import FastAPI, Request

from pydantic import BaseModel
from typing import Dict, List, Tuple

app = FastAPI()

import application.db as db

from application.db.tables import Product

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=db.engine)
session = Session()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
async def read_root():
    return {"message": "this is the get root of the application"}


@app.get("/id/{id}/")
async def read_id(id: str):
    return {"message": f"this is a get example with an id = {id}"}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    elif model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/query_parameters/")
async def example_query(par: str = None):
    return {"message": f"the query parameter is par = {par}"}


class Item(BaseModel):
    name: str
    price: float


@app.post("/post_example/")
async def example_post(item: Item):
    return {"message": f"validator passed for item = {item}"}


class ProductBase(BaseModel):
    name: str
    price: float


@app.post("/create_product/")
async def create_product(request: Request, product_base: ProductBase):
    payload = await request.json()
    product_created = Product(name=payload['name'], price=payload['price'])
    session.add(product_created)
    session.commit()
    print(product_created.id)
    print(session.query(Product).filter_by(name='leche'))
    print(session.query(Product).filter_by(price=2).all())
    print(session.query(Product).filter(Product.price > 1).all())
    print(session.query(Product).get(1).price)
    product_to_update = session.query(Product).filter_by(id=1).first()
    product_to_update.price = 3
    session.commit()
    session.query(Product).filter_by(name='leche').update({'name': 'queso'})
    session.commit()
    return {"message": "Worked!"}
