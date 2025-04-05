from fastapi import APIRouter, HTTPException, status, Depends

from src.infrastructure.exceptions.db_exceptions import DoesNotExist
from src.services.account_management.application.exceptions.user import UserExistException
from src.services.account_management.application.handler.user import UserHandler
from src.services.account_management.routers.dependencies.dependencies import Dependencies
from src.services.account_management.schemas.extensions.user import ToGetUser
from src.services.account_management.schemas.responses.user import UserAddedSuccessfully, GetUser, \
    UserDeletedSuccessfully, UserDeletedUnSuccessfully
from src.services.account_management.schemas.user import UserDto
from src.shared.account.user import UserEntity

user_router = APIRouter()

@user_router.post(path="", status_code=status.HTTP_200_OK)
async def add_user(user_dto: UserDto, user_handler: UserHandler =
                     Depends(Dependencies.user_handler)) -> UserAddedSuccessfully:
    try:
        public_id = await user_handler.add_user(user_dto)
        return UserAddedSuccessfully(public_id=public_id)

    except UserExistException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user_router.get(path="", status_code=status.HTTP_200_OK)
async def get_user(user_public_id: str, user_handler: UserHandler =
                     Depends(Dependencies.user_handler)) -> GetUser:
    try:
        user: UserEntity = await user_handler.get_user(user_public_id)
        return user @ ToGetUser()

    except DoesNotExist as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@user_router.delete(path="", status_code=status.HTTP_200_OK)
async def delete_user(user_public_id: str, user_handler: UserHandler =
                     Depends(Dependencies.user_handler)) -> UserDeletedSuccessfully:
    try:
        is_deleted = await user_handler.remove_user(user_public_id)

        if is_deleted:
            return UserDeletedSuccessfully()

        else:
            raise UserDeletedUnSuccessfully()

    except DoesNotExist as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
