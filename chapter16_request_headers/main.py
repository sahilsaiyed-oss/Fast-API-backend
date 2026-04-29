from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Request Headers Example"}


# Read custom header
@app.get("/user-agent")
def get_user_agent(user_agent: str = Header(...)):
    return {
        "user_agent": user_agent
    }


# Read authorization header
@app.get("/auth")
def get_auth_header(authorization: str = Header(...)):
    return {
        "authorization_header": authorization
    }


# Multiple headers
@app.get("/headers")
def get_headers(
    user_agent: str = Header(...),
    host: str = Header(...)
):
    return {
        "user_agent": user_agent,
        "host": host
    }