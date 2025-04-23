from fastapi import APIRouter

from src.api.exceptions import EndpointUnimplementedException

router = APIRouter()


@router.get("/", include_in_schema=False)
async def healthcheck():
    raise EndpointUnimplementedException(message="Router's Healthcheck not implemented")
