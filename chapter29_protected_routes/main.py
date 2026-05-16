from fastapi import FastAPI, Depends
from dependencies.auth_dependency import get_current_user

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Protected Routes Example"}


@app.get("/dashboard")
def dashboard(user=Depends(get_current_user)):

    return {
        "message": "Welcome to Dashboard",
        "user": user
    }