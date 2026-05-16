from fastapi import FastAPI

from database.connection import engine, Base
from routes.user_routes import router as user_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)


@app.get("/")
def root():
    return {
        "message": "Final FastAPI Project Running"
    }