# Chapter 04 - Path Parameters in FastAPI

## Introduction
Path parameters are values passed directly in the URL path. They are used to identify specific resources such as a user, product, or order.

Example:
/items/10

---

## What I Learned Today
- How to use path parameters in FastAPI
- Difference between path parameters and query parameters
- Passing values directly in the URL
- Using multiple path parameters
- Combining path and query parameters
- Basic validation using Python conditions

---

## Code Implementation

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/{username}")
def get_user(username: str):
    return {"username": username}

@app.get("/orders/{order_id}/items/{item_id}")
def get_order_item(order_id: int, item_id: int):
    return {
        "order_id": order_id,
        "item_id": item_id
    }

@app.get("/products/{product_id}")
def get_product(product_id: int, discount: float = 0):
    return {
        "product_id": product_id,
        "discount": discount
    }

@app.get("/students/{age}")
def get_student(age: int):
    if age < 18:
        return {"message": "Minor"}
    return {"message": "Adult"}

@app.get("/category/{category_name}")
def get_category(category_name: str):
    return {"category": category_name}