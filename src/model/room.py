from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class RoomOrm(Base):
    __tablename__ = "room"

    room_id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column()
    description: Mapped[str] = mapped_column(String(10000))
