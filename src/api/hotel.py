import json

from fastapi import APIRouter

# from fastapi_cache.decorator import cache
from src.dependencies import DBDep, redis_manager
from src.schema.hotel import HotelAdd, HotelPatch
from src.service.hotel import HotelService
from src.task.celery_app import celery_instance

router = APIRouter()


# @router.get("")
# @cache(expire=10)
# async def get_all(db: DBDep):
#     hotel = await HotelService(db).get_all()
#     return {"status": "ok", "data": hotel}


@router.get("")
async def get_all(db: DBDep):
    celery_instance.send_task("task_1")
    hotel_for_cache = await redis_manager.get("hotel")

    if not hotel_for_cache:
        hotel_for_db = await HotelService(db).get_all()
        hotel_dict = [model.model_dump() for model in hotel_for_db]
        hotel_json = json.dumps(hotel_dict)
        await redis_manager.set("hotel", hotel_json, 10)
        return hotel_for_db
    else:
        hotel_dict_valid = json.loads(hotel_for_cache)
        return hotel_dict_valid


@router.get("/hotel_id")
async def get_one_or_none(db: DBDep, hotel_id: int):
    hotel = await HotelService(db).get_one_or_none(hotel_id=hotel_id)
    return {"status": "ok", "data": hotel}


@router.post("")
async def post(db: DBDep, data: HotelAdd):
    hotel = await HotelService(db).post(data=data)
    return {"status": "ok", "data": hotel}


@router.put("/hotel_id")
async def put(db: DBDep, data: HotelAdd, hotel_id: int):
    hotel = await HotelService(db).put(data=data, hotel_id=hotel_id)
    return {"status": "ok", "data": hotel}


@router.patch("/hotel_id")
async def patch(db: DBDep, data: HotelPatch, hotel_id: int):
    hotel = await HotelService(db).patch(data=data, hotel_id=hotel_id)
    return {"status": "ok", "data": hotel}


@router.delete("/hotel_id")
async def delete(db: DBDep, hotel_id: int):
    hotel = await HotelService(db).delete(hotel_id=hotel_id)
    return {"status": "ok", "data": hotel}
