import uuid

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: uuid.UUID
    username: str
    email: str


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserResponse(BaseModel):
    id: uuid.UUID
    username: str
    email: str
