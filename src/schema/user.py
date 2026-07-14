from pydantic import BaseModel, EmailStr


class UserAddRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserAdd(BaseModel):
    name: str
    email: EmailStr
    hashed_password: str


class UserPatch(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    hashed_password: str | None = None


class UserData(UserAdd):
    user_id: int
