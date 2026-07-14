from src.model.hotel import HotelOrm
from src.repositories.base import BaseRepository
from src.schema.hotel import HotelData


class HotelRepository(BaseRepository):
    model = HotelOrm
    schema = HotelData
