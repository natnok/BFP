from fastapi import APIRouter

from src.dependencies import DBDep
from src.schema.room import RoomAdd, RoomPatch
from src.service.room import RoomService

router = APIRouter()


@router.get("")
async def get_all(db: DBDep):
    room = await RoomService(db).get_all()
    return {"status": "ok", "data": room}


@router.get("/room_id")
async def get_one_or_none(db: DBDep, room_id: int):
    room = await RoomService(db).get_one_or_none(room_id=room_id)
    return {"status": "ok", "data": room}


@router.post("")
async def post(db: DBDep, data: RoomAdd):
    room = await RoomService(db).post(data=data)
    return {"status": "ok", "data": room}


@router.put("/room_id")
async def put(db: DBDep, data: RoomAdd, room_id: int):
    room = await RoomService(db).put(data=data, room_id=room_id)
    return {"status": "ok", "data": room}


@router.patch("/room_id")
async def patch(db: DBDep, data: RoomPatch, room_id: int):
    room = await RoomService(db).patch(data=data, room_id=room_id)
    return {"status": "ok", "data": room}


@router.delete("/room_id")
async def delete(db: DBDep, room_id: int):
    room = await RoomService(db).get_one_or_none(room_id=room_id)
    return {"status": "ok", "data": room}
