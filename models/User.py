import uuid

from sqlalchemy.orm import Mapped, mapped_column

from models.BaseModel import EntityMeta, generate_uuid
from sqlalchemy import (
    Column,
    UUID,
    Integer,
    String,
    PrimaryKeyConstraint,
    Boolean,
    Float,
    TIMESTAMP,
    ForeignKey
)


class User(EntityMeta):
    __tablename__ = "user"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]

