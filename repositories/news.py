from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from configs.Database import get_db_connection
from models.news import News
from repositories.mixins.crud import CRUDRepositoryMixin


class NewsRepository(CRUDRepositoryMixin):
    def __init__(self, db: AsyncSession = Depends(get_db_connection)):
        super().__init__(News, db)
