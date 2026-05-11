from fastapi.responses import JSONResponse


async def custom_404_handler(request, exc):

    return JSONResponse(
        status_code=404,
        content={
            "error": "Custom Not Found Error",
            "message": "Requested resource does not exist"
        }
    )