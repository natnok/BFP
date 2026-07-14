from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from src.api import api_routers
from src.config import settings
from src.dependencies import redis_manager

# from src.task.celery_app import celery_instance


@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_manager.connect()
    # celery_instance.send_task("task_2")
    FastAPICache.init(RedisBackend(redis_manager._redis), prefix="fastapi-cache")
    yield
    await redis_manager.close()


app = FastAPI(
    lifespan=lifespan,
    title=settings.app_title,
    version=settings.app_version,
)

app.include_router(api_routers)


if __name__ == "__main__":
    uvicorn.run(
        app="src.main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=True,
    )
