from fastapi import FastAPI

app = FastAPI()

# Basic path parameter
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}


# String path parameter
@app.get("/users/{username}")
def get_user(username: str):
    return {"username": username}


# Multiple path parameters
@app.get("/orders/{order_id}/items/{item_id}")
def get_order_item(order_id: int, item_id: int):
    return {
        "order_id": order_id,
        "item_id": item_id
    }


# Path + Query parameter
@app.get("/products/{product_id}")
def get_product(product_id: int, discount: float = 0):
    return {
        "product_id": product_id,
        "discount": discount
    }


# Validation logic
@app.get("/students/{age}")
def get_student(age: int):
    if age < 18:
        return {"message": "Minor"}
    return {"message": "Adult"}


# Another real-world example
@app.get("/category/{category_name}")
def get_category(category_name: str):
    return {
        "category": category_name
    }