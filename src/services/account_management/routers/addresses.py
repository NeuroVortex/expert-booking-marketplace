from fastapi import APIRouter, HTTPException, status, Depends

from src.services.account_management.application.handler.user_address_handler import UserAddressHandler
from src.services.account_management.routers.dependencies.dependencies import Dependencies
from src.services.account_management.schemas.address import UserAddressDto
from src.shared.account.user import UserEntity

address_router = APIRouter()

@address_router.post(path="", status_code=status.HTTP_200_OK)
async def add_address(user_address_dto: UserAddressDto, user_address_handler: UserAddressHandler =
                     Depends(Dependencies.user_address_handler)) -> UserAddedSuccessfully:
    try:
        public_id = await user_address_handler.(user_dto)
        return UserAddedSuccessfully(public_id=public_id)

    except UserExistException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@address_router.get(path="", status_code=status.HTTP_200_OK)
async def get_addresses_by_user(user_public_id: str, user_handler: UserHandler =
                     Depends(Dependencies.user_handler)) -> GetUser:
    try:
        user: UserEntity = await user_handler.get_user(user_public_id)
        return user @ ToGetUser()

    except DoesNotExist as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@address_router.delete(path="", status_code=status.HTTP_200_OK)
async def delete_address(user_public_id: str, user_handler: UserHandler =
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
