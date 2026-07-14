from pydantic import BaseModel


class RoomAdd(BaseModel):
    number: int
    description: str


class RoomPatch(BaseModel):
    number: int | None = None
    description: str | None = None


class RoomData(RoomAdd):
    room_id: int
