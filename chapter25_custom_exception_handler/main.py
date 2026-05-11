from fastapi import FastAPI, HTTPException, Request
from exceptions.handlers import custom_404_handler

app = FastAPI()

app.add_exception_handler(404, custom_404_handler)


@app.get("/")
def root():
    return {"message": "Custom Exception Handler Working"}


@app.get("/items/{item_id}")
def get_item(item_id: int):

    if item_id > 10:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return {"item_id": item_id}