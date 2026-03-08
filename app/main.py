from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Automation API Service",
    description="Service for running automation tasks through API endpoints",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Automation API Service is running"}