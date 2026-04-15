from fastapi import FastAPI

app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to Chapter 02 - Routing"}

# Static routes
@app.get("/about")
def about():
    return {"info": "This is the about page of FastAPI project"}

@app.get("/contact")
def contact():
    return {
        "email": "sahil@example.com",
        "phone": "1234567890"
    }

# Dynamic route (Path Parameter)
@app.get("/user/{username}")
def get_user(username: str):
    return {"user": username}

# Another dynamic example
@app.get("/product/{product_id}")
def get_product(product_id: int):
    return {
        "product_id": product_id,
        "status": "Available"
    }