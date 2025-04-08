from src.schema.location import GetLocation
from src.schema.profile import GetProfile
from src.schema.user import GetUser
from src.shared.account.user import UserEntity


class ToGetUser:
    def __rmatmul__(self, user: UserEntity) -> GetUser:
        return GetUser(
            public_id=str(user.user_public_id),
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            phone=user.phone,
            identifier=user.identifier,
            gender=user.gender.name,
            profile=GetProfile(name=user.profile.name,
                               location=GetLocation(**user.profile.location._asdict()))
        )