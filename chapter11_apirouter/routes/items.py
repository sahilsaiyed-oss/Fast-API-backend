from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["Items"])

items_db = [
    {"id": 1, "name": "Laptop"},
    {"id": 2, "name": "Phone"}
]

@router.get("/")
def get_items():
    return {"items": items_db}

@router.get("/{item_id}")
def get_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}