from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from convertors.User import UserCreateToUser, UserToUserResponse
from models.User import User
from schemas.AuthSchema import Token
from schemas.UserSchema import UserResponse, UserCreate
from services.Auth import get_current_user, AuthService
from services.User import UserService
from utils.wrappers import error_wrapper

router = APIRouter(prefix="/api/v1/users", tags=["user"])


@router.post("/token/", response_model=Token)
async def get_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        auth_service: AuthService = Depends(),
):
    user = error_wrapper(auth_service.authenticate_user, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta()
    access_token = auth_service.create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get(
    "/me/",
    description="Получение информации о текущем User",
    response_model=UserResponse,
)
async def get_me(
        current_user: User = Depends(get_current_user)
):
    return UserToUserResponse(current_user)


@router.post(
    "/",
    description="создание User",
    response_model=UserResponse,
)
async def create(user: UserCreate, user_service: UserService = Depends()):
    user = UserCreateToUser(user)
    user = error_wrapper(user_service.create, user)
    user = UserToUserResponse(user)
    return user
