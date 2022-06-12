from app.api.routes import route_file
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(route_file.router, prefix="/file", tags=["file"])