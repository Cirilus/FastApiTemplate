import uuid
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from models.BaseModel import EntityMeta


class User(EntityMeta):
    __tablename__ = "user"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    username: Mapped[str]
    password: Mapped[str]

    email: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(nullable=True)

    created_at: Mapped[datetime] = mapped_column(default=func.now, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now, onupdate=func.now, nullable=False
    )
