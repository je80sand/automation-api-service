import logging
import time

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.routes import router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI(
    title="Automation API Service",
    description="A REST API that runs automated infrastructure checks such as API health monitoring.",
    version="1.0.0",
    contact={
        "name": "Jose Sandoval",
        "github": "https://github.com/je80sand"
    }
)

app.include_router(router)

REQUEST_LOG = {}
RATE_LIMIT = 5
WINDOW_SECONDS = 60


@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host if request.client else "unknown"
    current_time = time.time()

    if client_ip not in REQUEST_LOG:
        REQUEST_LOG[client_ip] = []

    REQUEST_LOG[client_ip] = [
        timestamp for timestamp in REQUEST_LOG[client_ip]
        if current_time - timestamp < WINDOW_SECONDS
    ]

    if len(REQUEST_LOG[client_ip]) >= RATE_LIMIT:
        return JSONResponse(
            status_code=429,
            content={"detail": "Rate limit exceeded. Try again later."}
        )

    REQUEST_LOG[client_ip].append(current_time)

    response = await call_next(request)
    return response


@app.get("/")
def root():
    return {"message": "Automation API Service is running"}