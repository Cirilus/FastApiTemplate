import uuid
from typing import Type, List

from fastapi import Depends
from loguru import logger
from sqlalchemy.orm import Session

from configs.Database import get_db_connection
from models.User import User
from utils.errors import ErrEntityNotFound


class UserRepository:
    def __init__(self, db: Session = Depends(get_db_connection)):
        self.db = db

    def get_by_login(self, login: str) -> Type[User]:
        logger.debug("User - Repository - get_by_login")
        user = self.db.query(User).filter_by(login=login).first()
        if user is None:
            raise ErrEntityNotFound("the entity not found")
        return user

    def get_by_id(self, id: uuid.UUID) -> Type[User]:
        logger.debug("User - Repository - get_by_id")
        user = self.db.get(
            User,
            id
        )
        if user is None:
            raise ErrEntityNotFound("the entity not found")
        return user

    def get_list(self) -> List[Type[User]]:
        logger.debug("User - Repository - get_list")
        users = self.db.query(User).all()
        return users

    def create(self, user: User) -> User:
        logger.debug("User - Repository - create")
        user.id = uuid.uuid4()
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update(self, id: uuid.UUID, user: User) -> User:
        logger.debug("User - Repository - update")
        user.id = id
        self.db.merge(user)
        self.db.commit()
        return user

    def delete(self, user: User) -> None:
        logger.debug("User - Repository - delete")
        self.db.delete(user)
        self.db.commit()
        self.db.flush()
