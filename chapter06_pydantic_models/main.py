from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

# Basic Pydantic Model with validation
class Product(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)
    description: str | None = Field(default=None, max_length=200)


@app.post("/products")
def create_product(product: Product):
    return {
        "message": "Product created successfully",
        "product": product
    }


# User model with email validation
class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    age: int = Field(..., ge=18, le=60)


@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "user": user
    }


# Nested Model Example
class Address(BaseModel):
    city: str
    state: str
    pincode: int


class Customer(BaseModel):
    name: str
    address: Address


@app.post("/customers")
def create_customer(customer: Customer):
    return {
        "message": "Customer created successfully",
        "customer": customer
    }


# Response Model Example
@app.get("/sample-product", response_model=Product)
def get_sample_product():
    return {
        "name": "Laptop",
        "price": 50000,
        "quantity": 5,
        "description": "High performance laptop"
    }