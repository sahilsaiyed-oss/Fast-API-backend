from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory storage (temporary database)
items_db = []

# Model
class Item(BaseModel):
    id: int
    name: str
    price: float


# CREATE
@app.post("/items")
def create_item(item: Item):
    items_db.append(item)
    return {
        "message": "Item added",
        "data": item
    }


# READ ALL
@app.get("/items")
def get_items():
    return {
        "items": items_db
    }


# READ SINGLE
@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


# UPDATE
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db[index] = updated_item
            return {
                "message": "Item updated",
                "data": updated_item
            }
    raise HTTPException(status_code=404, detail="Item not found")


# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            deleted_item = items_db.pop(index)
            return {
                "message": "Item deleted",
                "data": deleted_item
            }
    raise HTTPException(status_code=404, detail="Item not found")