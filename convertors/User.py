from models.User import User
from schemas.UserSchema import UserCreate, UserResponse


def UserCreateToUser(user: UserCreate) -> User:
    result = User(
        id=None,
        login=user.login,
        password=user.password,
    )
    return result


def UserToUserResponse(user: User) -> UserResponse:
    result = UserResponse(
        id=user.id,
        login=user.login,
    )
    return result