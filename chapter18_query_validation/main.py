from fastapi import FastAPI, Query

app = FastAPI()


# Basic validation
@app.get("/items")
def get_items(
    limit: int = Query(10, ge=1, le=100)
):
    return {
        "message": f"Showing {limit} items"
    }


# String length validation
@app.get("/search")
def search_items(
    q: str = Query(..., min_length=3, max_length=50)
):
    return {
        "search_query": q
    }


# Regex / Pattern validation
@app.get("/users")
def get_user(
    username: str = Query(..., pattern="^[a-zA-Z0-9_]+$")
):
    return {
        "username": username
    }


# Multiple validated query params
@app.get("/products")
def get_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
    sort: str = Query("asc", pattern="^(asc|desc)$")
):
    return {
        "page": page,
        "limit": limit,
        "sort": sort
    }