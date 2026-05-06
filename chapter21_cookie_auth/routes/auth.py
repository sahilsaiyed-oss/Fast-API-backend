from fastapi import APIRouter, Response, Cookie
from utils.cookie_manager import set_session_cookie, delete_session_cookie

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.get("/login")
def login(response: Response):
    set_session_cookie(response)
    return {"message": "Logged In Successfully"}


@router.get("/profile")
def profile(session_id: str = Cookie(None)):
    if not session_id:
        return {"message": "Not Logged In"}

    return {
        "message": "Profile Accessed",
        "session_id": session_id
    }


@router.get("/logout")
def logout(response: Response):
    delete_session_cookie(response)
    return {"message": "Logged Out Successfully"}