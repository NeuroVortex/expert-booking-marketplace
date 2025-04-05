from src.services.account_management.domain.profile import Profile
from src.services.account_management.domain.providers.gender import Gender
from src.services.account_management.schemas.responses.location import GetLocation
from src.services.account_management.schemas.responses.profile import GetProfile
from src.services.account_management.schemas.responses.user import GetUser
from src.services.account_management.schemas.user import UserDto
from src.shared.account.user import UserEntity


class ToUserEntity:
    def __rmatmul__(self, user_dto: UserDto) -> UserEntity:
        return UserEntity(
            id=None,
            user_public_id=None,
            first_name=user_dto.first_name,
            last_name=user_dto.last_name,
            phone=user_dto.phone,
            email=user_dto.email,
            gender=Gender[user_dto.gender.lower().capitalize()],
            identifier=user_dto.identifier,
            profile=Profile(**user_dto.profile.model_dump())
        )

class ToGetUser:
    def __rmatmul__(self, user: UserEntity) -> GetUser:
        return GetUser(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            phone=user.phone,
            identifier=user.identifier,
            gender=user.gender.name,
            profile=GetProfile(name=user.profile.name,
                               location=GetLocation(**user.profile.location._asdict()))
        )