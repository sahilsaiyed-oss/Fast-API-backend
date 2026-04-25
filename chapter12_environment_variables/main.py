from fastapi import FastAPI
import os

app = FastAPI()

# Reading environment variables
APP_NAME = os.getenv("APP_NAME", "FastAPI App")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
DEBUG_MODE = os.getenv("DEBUG", "False")


@app.get("/")
def root():
    return {
        "app_name": APP_NAME,
        "version": APP_VERSION,
        "debug": DEBUG_MODE
    }


@app.get("/config")
def get_config():
    return {
        "message": "Environment variables loaded successfully",
        "app_name": APP_NAME,
        "version": APP_VERSION,
        "debug": DEBUG_MODE
    }


@app.get("/status")
def status():
    if DEBUG_MODE == "True":
        return {"status": "Development Mode"}
    return {"status": "Production Mode"}