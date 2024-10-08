import uuid
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from models.BaseModel import EntityMeta


class News(EntityMeta):
    __tablename__ = "news"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)

    created_at: Mapped[datetime] = mapped_column(default=func.now, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now, onupdate=func.now, nullable=False
    )
