from fastapi import FastAPI, Request
import time

app = FastAPI()


# Custom Middleware
@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)

    print(f"Request: {request.method} {request.url}")
    print(f"Processed in {process_time:.4f} seconds")

    return response


@app.get("/")
def root():
    return {"message": "Middleware Working Successfully"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {"product_id": product_id}