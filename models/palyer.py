import uuid
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from models.BaseModel import EntityMeta


class Player(EntityMeta):
    __tablename__ = "player"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    firstname: Mapped[str] = mapped_column(nullable=False)
    middelname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=False)

    played_from: Mapped[datetime] = mapped_column(nullable=False)

    biography: Mapped[str] = mapped_column(nullable=False)
    position: Mapped[str] = mapped_column(nullable=False)
    achievements: Mapped[str] = mapped_column(nullable=False)
