from src.services.account_management.domain.profile import Profile
from src.services.account_management.domain.providers.gender import Gender
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