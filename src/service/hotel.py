from src.schema.hotel import HotelAdd, HotelPatch
from src.service.base import BaseService


class HotelService(BaseService):
    async def get_all(self):
        return await self.db.hotel.get_all()

    async def get_one_or_none(self, hotel_id: int):
        return await self.db.hotel.get_one_or_none(hotel_id=hotel_id)

    async def post(self, data: HotelAdd):
        hotel = await self.db.hotel.post(data=data)
        await self.db.commit()
        return hotel

    async def put(self, data: HotelAdd, hotel_id: int):
        hotel = await self.db.hotel.put(data=data, hotel_id=hotel_id)
        await self.db.commit()
        return hotel

    async def patch(self, data: HotelPatch, hotel_id: int, exclude_unset: bool = True):
        hotel = await self.db.hotel.put(data=data, hotel_id=hotel_id, exclude_unset=exclude_unset)
        await self.db.commit()
        return hotel

    async def delete(self, hotel_id: int):
        hotel = await self.db.hotel.delete(hotel_id=hotel_id)
        await self.db.commit()
        return hotel
