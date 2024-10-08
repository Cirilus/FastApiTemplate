from fastapi import Depends

from repositories.news import NewsRepository
from services.mixins.crud import CRUDServiceMixin


class NewsService(CRUDServiceMixin):
    def __init__(self, repo: NewsRepository = Depends()):
        super().__init__(repo)
