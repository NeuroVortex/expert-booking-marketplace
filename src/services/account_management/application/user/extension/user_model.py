from src.services.account_management.schema.user import User as _UserModel
from src.shared.contract.personage.gender import Gender
from src.shared.contract.personage.profile import Profile
from src.shared.contract.personage.user import User


class ToUserModel:
    def __rmatmul__(self, user: User) -> _UserModel:
        return _UserModel(
            first_name=user.first_name,
            last_name=user.last_name,
            primary_email=user.email,
            primary_phone=user.phone,
            gender=user.gender.name,
            identifier= user.identifier,
            profile=user.profile._asdict(),
            extras=user.extras,
            is_archived=user.is_archived)

class ToUser:
    def __rmatmul__(self, user: _UserModel) -> User:
        return User(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.primary_email,
            phone=user.primary_phone,
            gender=Gender[user.gender],
            identifier= user.identifier,
            profile=Profile(**user.profile),
            extras=user.extras,
            is_archived=user.is_archived)
