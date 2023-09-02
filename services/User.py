from typing import Annotated, Type, List

import uuid
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from loguru import logger
from passlib.context import CryptContext

from configs.Environment import get_environment_variables
from models.User import User
from repositories.User import UserRepository
from utils.errors import ErrUnAuthorized


class UserService:
    def __init__(self, user_repo: UserRepository = Depends()):
        self.user_repo = user_repo
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_password_hash(self, password) -> str:
        return self.pwd_context.hash(password)

    def get_by_login(self, login: str) -> Type[User]:
        logger.debug("User - Repository - get_by_login")
        return self.user_repo.get_by_login(login)

    def get_by_id(self, id: uuid.UUID) -> Type[User]:
        logger.debug("User - Repository - get_by_id")
        return self.user_repo.get_by_id(id)

    def get_list(self) -> List[Type[User]]:
        logger.debug("User - Repository - get_list")
        return self.user_repo.get_list()

    def create(self, user: User) -> User:
        logger.debug("User - Repository - create")
        user.password = self.get_password_hash(user.password)
        return self.user_repo.create(user)

    def update(self, id: uuid.UUID, user: User) -> User:
        logger.debug("User - Repository - update")
        return self.user_repo.update(id, user)

    def delete(self, user: User) -> None:
        logger.debug("User - Repository - delete")
        self.user_repo.delete(user)
        return None
