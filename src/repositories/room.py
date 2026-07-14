from src.model.room import RoomOrm
from src.repositories.base import BaseRepository
from src.schema.room import RoomData


class RoomRepository(BaseRepository):
    model = RoomOrm
    schema = RoomData
