from fastapi import FastAPI

from src.api.routers import router as api_router
from src.config.lifespan import lifespan
from src.config.conf_logger import setup_logger

logger = setup_logger(__name__, "main")

app = FastAPI(lifespan=lifespan)
app.include_router(api_router, prefix="/api", tags=["api"])


@app.get("/")
async def healthcheck():
    logger.info("Called first healthcheck")
    return {"status": "OK"}
