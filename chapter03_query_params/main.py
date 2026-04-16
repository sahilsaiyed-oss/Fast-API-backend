from fastapi import FastAPI

app = FastAPI()

# Basic query parameter
@app.get("/items")
def get_items(name: str):
    return {"item_name": name}

# Multiple query parameters
@app.get("/products")
def get_products(name: str, price: float):
    return {
        "product_name": name,
        "product_price": price
    }

# Optional query parameter
@app.get("/users")
def get_users(age: int = None):
    if age:
        return {"message": f"Users filtered by age {age}"}
    return {"message": "All users"}

# Default value
@app.get("/orders")
def get_orders(limit: int = 10):
    return {"message": f"Showing {limit} orders"}

# Combination example (real-world style)
@app.get("/search")
def search(q: str, page: int = 1, limit: int = 10):
    return {
        "query": q,
        "page": page,
        "limit": limit
    }