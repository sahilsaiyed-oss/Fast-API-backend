from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Full Internal Model
class UserDB(BaseModel):
    id: int
    username: str
    email: str
    password: str


# Safe Public Response Model
class UserResponse(BaseModel):
    id: int
    username: str
    email: str


fake_user_db = {
    "id": 1,
    "username": "sahil",
    "email": "sahil@example.com",
    "password": "supersecret"
}


@app.get("/user", response_model=UserResponse)
def get_user():
    return fake_user_db


# Product Example
class Product(BaseModel):
    id: int
    name: str
    price: float


@app.get("/product", response_model=Product)
def get_product():
    return {
        "id": 101,
        "name": "Laptop",
        "price": 55000,
        "extra_field": "This will be hidden"
    }


# List Response Model Example
@app.get("/products", response_model=list[Product])
def get_products():
    return [
        {"id": 1, "name": "Phone", "price": 20000},
        {"id": 2, "name": "Tablet", "price": 30000}
    ]