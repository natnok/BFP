from src.schema.room import RoomAdd, RoomPatch
from src.service.base import BaseService


class RoomService(BaseService):
    async def get_all(self):
        return await self.db.room.get_all()

    async def get_one_or_none(self, room_id: int):
        return await self.db.room.get_one_or_none(room_id=room_id)

    async def post(self, data: RoomAdd):
        room = await self.db.room.post(data=data)
        await self.db.commit()
        return room

    async def put(self, data: RoomAdd, room_id: int):
        room = await self.db.room.put(data=data, room_id=room_id)
        await self.db.commit()
        return room

    async def patch(self, data: RoomPatch, room_id: int, exclude_unset: bool = True):
        room = await self.db.room.put(data=data, room_id=room_id, exclude_unset=exclude_unset)
        await self.db.commit()
        return room

    async def delete(self, room_id: int):
        room = await self.db.room.delete(room_id=room_id)
        await self.db.commit()
        return room
