from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend origins
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:5500",
    "https://myfrontend.com"
]

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def root():
    return {"message": "CORS Configured Successfully"}


@app.get("/data")
def get_data():
    return {
        "name": "Sahil",
        "role": "Backend Developer"
    }


@app.post("/submit")
def submit_data():
    return {"message": "Data submitted successfully"}