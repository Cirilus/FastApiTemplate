import uuid

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: uuid.UUID
    login: str
    password: str


class UserCreate(BaseModel):
    login: str
    password: str


class UserResponse(BaseModel):
    id: uuid.UUID
    login: str
