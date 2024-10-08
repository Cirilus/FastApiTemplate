import uuid
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from models.BaseModel import EntityMeta


class Match(EntityMeta):
    __tablename__ = "match"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    opponent_team: Mapped[str] = mapped_column(nullable=False)

    date: Mapped[datetime] = mapped_column(nullable=False)

    result: Mapped[str] = mapped_column(nullable=False)

    stadium: Mapped[str] = mapped_column(nullable=False)
