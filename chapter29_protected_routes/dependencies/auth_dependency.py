from fastapi import Header, HTTPException
from auth.verify_token import verify_token


def get_current_user(authorization: str = Header(...)):

    token = authorization.replace("Bearer ", "")

    payload = verify_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    return payload