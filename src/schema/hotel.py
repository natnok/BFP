from pydantic import BaseModel


class HotelAdd(BaseModel):
    title: str
    description: str
    stars: int


class HotelPatch(BaseModel):
    title: str | None = None
    description: str | None = None
    stars: int | None = None


class HotelData(HotelAdd):
    hotel_id: int
