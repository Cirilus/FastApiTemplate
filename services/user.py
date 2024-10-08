from fastapi import Depends

from repositories.user import UserRepository
from services.mixins.crud import CRUDServiceMixin


class UserService(CRUDServiceMixin):
    def __init__(self, repo: UserRepository = Depends()):
        super().__init__(repo)
