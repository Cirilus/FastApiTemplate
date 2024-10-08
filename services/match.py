from fastapi import Depends

from repositories.match import MatchRepository
from services.mixins.crud import CRUDServiceMixin


class MatchService(CRUDServiceMixin):
    def __init__(self, repo: MatchRepository = Depends()):
        super().__init__(repo)
