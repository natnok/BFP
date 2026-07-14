from fastapi import HTTPException


class FapExceptionBase(Exception):
    detail: str = "Неожиданная ошибка"

    def __init__(self):
        super().__init__(self.detail)


class FapExceptionHttp(HTTPException):
    status_code: int = 500
    detail: str = "Неожиданная ошибка"

    def __init__(self, *args, **kwargs):
        super().__init__(detail=self.detail, status_code=self.status_code, *args, **kwargs)


class EmailError(FapExceptionBase):
    detail: str = "Некорректная почта"


class EmailErrorHttp(FapExceptionHttp):
    status_code: int = 401
    detail: str = "Некорректная почта"


class PasswordError(FapExceptionBase):
    detail: str = "Некорректный пароль"


class PasswordErrorHttp(FapExceptionHttp):
    status_code: int = 401
    detail: str = "Некорректный пароль"
