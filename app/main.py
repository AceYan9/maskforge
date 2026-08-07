import json
import time
import uuid
import logging.config

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.main import api_router
from app.config import settings
from app.logging_config import LOGGING_CONFIG, request_id_ctx
from app.utils.exception_handler import BizException


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

@app.middleware("http")
async def log_request_middleware(request: Request, call_next):
    start_time = time.time()
    request_id = str(uuid.uuid4())
    request_id_ctx.set(request_id)

    method = request.method
    url = str(request.url.path)

    query_params = dict(request.query_params)

    path_params = request.path_params

    body_bytes = await request.body()
    content_type = request.headers.get("content-type", "")
    body = None
    if body_bytes:
        if "application/json" in content_type:
            try:
                body = json.loads(body_bytes)
            except Exception:
                body = body_bytes.decode("utf-8", errors="replace")
        elif "multipart/form-data" in content_type:
            body = "<multipart/form-data>"
        else:
            body = body_bytes.decode("utf-8", errors="replace")

    async def receive():
        return {"type": "http.request", "body": body_bytes}

    request._receive = receive

    request_info = f"[{method}]{url}"

    logger.info(f"{request_info} - Query: {query_params}, Path: {path_params}, Body: {body}")

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    logger.info(f"{request_info} - Process time: {process_time:.2f}ms")

    return response

@app.exception_handler(BizException)
async def global_exception_handler(request: Request, exc: BizException):
    error_msg = str(exc)
    logger.error(f"[{request.method}]{request.url.path} - {error_msg}")
    return JSONResponse(
        status_code=500,
        content={
            "message": error_msg,
        },
    )
