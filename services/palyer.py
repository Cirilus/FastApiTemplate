from fastapi import Depends

from repositories.palyer import PlayerRepository
from services.mixins.crud import CRUDServiceMixin


class PlayerService(CRUDServiceMixin):
    def __init__(self, repo: PlayerRepository = Depends()):
        super().__init__(repo)
