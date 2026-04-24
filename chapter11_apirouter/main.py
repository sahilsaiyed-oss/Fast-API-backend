from fastapi import FastAPI
from routes import items, users

app = FastAPI()

# Include routers
app.include_router(items.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Chapter 11 - APIRouter working"}