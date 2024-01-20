from application import init_sentry
init_sentry()

from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel, validator

app = FastAPI()


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

    @validator("price")
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError(f"we expect price >= 0, we received {value}")
        return value


@app.post("/post_example/")
async def example_post(item: Item):
    return {"message": f"validator passed for item = {item}"}
