from fastapi import FastAPI
from auth.jwt_handler import create_access_token
from schemas.auth_schema import LoginSchema

app = FastAPI()


@app.get("/")
def root():
    return {"message": "JWT Authentication Running"}


@app.post("/login")
def login(user: LoginSchema):

    token = create_access_token(
        {"sub": user.username}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }