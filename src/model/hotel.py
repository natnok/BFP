from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class HotelOrm(Base):
    __tablename__ = "hotel"

    hotel_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(1000))
    description: Mapped[str] = mapped_column(String(10000))
    stars: Mapped[int] = mapped_column()
