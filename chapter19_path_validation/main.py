from fastapi import FastAPI, Path

app = FastAPI()


# Numeric path validation
@app.get("/items/{item_id}")
def get_item(
    item_id: int = Path(..., ge=1, le=1000)
):
    return {
        "item_id": item_id
    }


# Product ID validation
@app.get("/products/{product_id}")
def get_product(
    product_id: int = Path(..., gt=0)
):
    return {
        "product_id": product_id
    }


# User age validation
@app.get("/users/{age}")
def get_user_by_age(
    age: int = Path(..., ge=18, le=60)
):
    return {
        "message": f"User age is {age}"
    }


# Order ID with title/description metadata
@app.get("/orders/{order_id}")
def get_order(
    order_id: int = Path(
        ...,
        ge=1,
        title="Order ID",
        description="Unique ID of the order"
    )
):
    return {
        "order_id": order_id
    }