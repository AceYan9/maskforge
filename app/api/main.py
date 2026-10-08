from fastapi import APIRouter

from app.api.routes import task_routes

version1_prefix = "/v1"


api_router = APIRouter(prefix=version1_prefix)
api_router.include_router(task_routes.router, prefix="/tasks", tags=["task"])
