from fastapi import APIRouter

from src.api import auth, hotel, room

api_routers = APIRouter()

api_routers.include_router(auth.router, prefix="/auth", tags=["auth"])
api_routers.include_router(hotel.router, prefix="/hotel", tags=["hotel"])
api_routers.include_router(room.router, prefix="/room", tags=["room"])
