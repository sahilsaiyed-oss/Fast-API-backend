from fastapi import FastAPI
import logging

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
def root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to Logging in FastAPI"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    logger.info(f"Fetching user with ID: {user_id}")
    return {"user_id": user_id}


@app.get("/error")
def simulate_error():
    try:
        result = 10 / 0
        return {"result": result}
    except ZeroDivisionError as e:
        logger.error(f"An error occurred: {str(e)}")
        return {"error": "Division by zero occurred"}


@app.get("/debug")
def debug_route():
    logger.debug("Debug endpoint accessed")
    return {"message": "Debug log generated"}