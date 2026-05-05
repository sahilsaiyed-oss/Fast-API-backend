from fastapi import FastAPI, Cookie

app = FastAPI()

@app.get("/profile")
def get_profile(session_id: str = Cookie(None)):
    if not session_id:
        return {"message": "No session cookie provided"}

    return {
        "message": "Profile Accessed",
        "session_id": session_id
    }


@app.get("/cookies")
def read_cookies(
    session_id: str = Cookie(None),
    theme: str = Cookie("light")
):
    return {
        "session_id": session_id,
        "theme": theme
    }