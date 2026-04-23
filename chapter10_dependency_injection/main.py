from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

# Fake database
items_db = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Phone", "price": 20000}
]

# Dependency function (common logic)
def get_item_by_id(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


# Endpoint using dependency
@app.get("/items/{item_id}")
def read_item(item = Depends(get_item_by_id)):
    return item


# Another dependency example
def verify_token(token: str):
    if token != "secret123":
        raise HTTPException(status_code=401, detail="Invalid token")
    return token


# Protected route using dependency
@app.get("/protected")
def protected_route(token: str, verified: str = Depends(verify_token)):
    return {
        "message": "Access granted",
        "token": verified
    }