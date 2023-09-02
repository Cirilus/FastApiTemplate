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
    id = Column(UUID, primary_key=True)
    login = Column(String, unique=True)
    password = Column(String)
