from src.repositories.hotel import HotelRepository
from src.repositories.room import RoomRepository
from src.repositories.user import UserRepository


class DBManager:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.hotel = HotelRepository(self.session)
        self.room = RoomRepository(self.session)
        self.user = UserRepository(self.session)

        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()
