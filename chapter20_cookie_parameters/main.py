from fastapi import FastAPI, Cookie

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Cookie Parameters Example"}


# Read single cookie
@app.get("/profile")
def get_profile(session_id: str = Cookie(...)):
    return {
        "message": "Profile Accessed",
        "session_id": session_id
    }


# Optional cookie
@app.get("/cart")
def get_cart(cart_id: str = Cookie(None)):
    if cart_id:
        return {"cart_id": cart_id}
    return {"message": "No cart cookie found"}


# Multiple cookies
@app.get("/cookies")
def read_cookies(
    session_id: str = Cookie(...),
    theme: str = Cookie("light")
):
    return {
        "session_id": session_id,
        "theme": theme
    }
