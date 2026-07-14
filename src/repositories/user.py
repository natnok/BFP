from src.model.user import UserOrm
from src.repositories.base import BaseRepository
from src.schema.user import UserData


class UserRepository(BaseRepository):
    model = UserOrm
    schema = UserData
