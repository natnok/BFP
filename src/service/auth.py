from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash

from src.config import settings
from src.dependencies import DBDep
from src.exception import EmailError, PasswordError
from src.schema.user import UserAdd, UserAddRequest
from src.service.base import BaseService


class AuthService(BaseService):
    password_hash = PasswordHash.recommended()

    def verify_password(self, plain_password, hashed_password):
        return self.password_hash.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.password_hash.hash(password)

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return encoded_jwt

    async def decode_user(self, db: DBDep, data: UserAddRequest):
        token = await AuthService(db).login_user(data=data)
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload
        
    async def register_user(self, data: UserAddRequest):
        hashed_password = self.get_password_hash(data.password)
        new_user_data = UserAdd(name=data.name, email=data.email, hashed_password=hashed_password)
        user = await self.db.user.post(data=new_user_data)
        await self.db.commit()
        return user

    async def login_user(self, data: UserAddRequest):
        user = await self.db.user.get_one_or_none(email=data.email)

        if not user:
            raise EmailError

        if not self.verify_password(data.password, hashed_password=user.hashed_password):  # pyright: ignore[reportAttributeAccessIssue]
            raise PasswordError

        access_token = self.create_access_token(data={"user_id": user.user_id})  # pyright: ignore[reportAttributeAccessIssue]
        return access_token
