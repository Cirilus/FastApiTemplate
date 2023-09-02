from datetime import timedelta, datetime
from typing import Type

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext

from configs.Environment import get_environment_variables
from models.User import User
from services.User import UserService
from utils.errors import ErrUnAuthorized


class AuthService:
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/token")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60

    def __init__(self, user_service: UserService = Depends()):
        self.user_service = user_service
        env = get_environment_variables()
        self.SECRET_KEY = env.SECRET_KEY
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, hashed_password) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password) -> str:
        return self.pwd_context.hash(password)

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    def authenticate_user(self, login: str, password: str) -> bool | Type[User]:
        user = self.user_service.get_by_login(login)
        if not user:
            return False
        if not self.verify_password(password, user.password):
            return False
        return user


def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/api/v1/users/token")),
                     auth_service: AuthService = Depends(),
                     user_service: UserService = Depends()) -> Type[User] | None:
    try:
        payload = jwt.decode(token, auth_service.SECRET_KEY, algorithms=[auth_service.ALGORITHM])
        username = payload.get("sub")
        user = user_service.get_by_login(username)
        if username is None or user is None:
            raise ErrUnAuthorized("the user not authorized")
    except JWTError:
        raise ErrUnAuthorized("the user not authorized")
    return user
