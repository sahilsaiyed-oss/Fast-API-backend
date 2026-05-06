from fastapi import Response


def set_session_cookie(response: Response):
    response.set_cookie(
        key="session_id",
        value="abc123xyz",
        max_age=3600
    )


def delete_session_cookie(response: Response):
    response.delete_cookie(key="session_id")