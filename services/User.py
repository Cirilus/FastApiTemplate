from typing import Annotated

from fastapi import Depends
from jose import jwt, JWTError

from services.Auth import AuthService
from utils.errors import ErrUNAUTHORIZED


class UserService:
    def __init__(self, auth_service: AuthService = Depends()):
        self.auth_service = auth_service

    async def get_current_user(self, token: Annotated[str, Depends(AuthService().oauth2_scheme)]):
        try:
            payload = jwt.decode(token, self.auth_service.SECRET_KEY, algorithms=[self.auth_service.ALGORITHM])
            username = payload.get("sub")
            if username is None:
                raise ErrUNAUTHORIZED
            print(username)
        except JWTError:
            raise ErrUNAUTHORIZED
        return username
