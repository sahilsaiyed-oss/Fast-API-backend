from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic model (Request Body structure)
class Item(BaseModel):
    name: str
    price: float
    quantity: int


# Basic POST request
@app.post("/items")
def create_item(item: Item):
    return {
        "message": "Item created successfully",
        "data": item
    }


# Another POST example
class User(BaseModel):
    username: str
    email: str
    age: int


@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "user": user
    }


# Mixed example (Path + Body)
@app.post("/orders/{order_id}")
def create_order(order_id: int, item: Item):
    return {
        "order_id": order_id,
        "item": item
    }


# Optional field example
class Product(BaseModel):
    name: str
    price: float
    description: str | None = None


@app.post("/products")
def create_product(product: Product):
    return {
        "message": "Product created",
        "product": product
    }