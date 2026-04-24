from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

users_db = [
    {"id": 1, "name": "Sahil"},
    {"id": 2, "name": "Ali"}
]

@router.get("/")
def get_users():
    return {"users": users_db}

@router.get("/{user_id}")
def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}