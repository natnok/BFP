from fastapi import APIRouter, Response

from src.dependencies import DBDep
from src.exception import EmailError, EmailErrorHttp, PasswordError, PasswordErrorHttp
from src.schema.user import UserAddRequest
from src.service.auth import AuthService

router = APIRouter()


@router.post("/register")
async def register(db: DBDep, data: UserAddRequest):
    user = await AuthService(db).register_user(data=data)
    return {"status": "ok", "data": user}


@router.post("/login")
async def login(db: DBDep, data: UserAddRequest, response: Response):

    try:
        access_token = await AuthService(db).login_user(data=data)
    except EmailError:
        raise EmailErrorHttp()
    except PasswordError:
        raise PasswordErrorHttp()

    response.set_cookie("access_token", access_token)
    return {"status": "ok", "access_token": access_token}


@router.post("/get_my")
async def get_my(db: DBDep, data: UserAddRequest):
    return await AuthService(db).decode_user(db, data=data)
