from src.services.account_management.domain.location import Location
from src.services.account_management.domain.providers.certificate import Certificate
from src.services.account_management.domain.providers.education import Education
from src.services.account_management.domain.providers.experience import Experience
from src.services.account_management.infrastructure.models.user import User
from src.services.account_management.domain.providers.gender import Gender
from src.services.account_management.domain.profile import Profile
from src.shared.account.user import UserEntity


class ToUserModel:
    def __rmatmul__(self, user: UserEntity) -> User:
        return User(
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
    def __rmatmul__(self, user: User) -> UserEntity:
        return UserEntity(
            id=user.id,
            user_public_id=user.public_id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.primary_email,
            phone=user.primary_phone,
            gender=Gender[user.gender],
            identifier= user.identifier,
            profile=Profile(
                name=user.profile["name"],
                location=Location(**user.profile["location"]),
                photo_path=user.profile["photo_path"],
                headline=user.profile["headline"],
                website=user.profile["website"],
                years_of_experience=user.profile["years_of_experience"],
                bio=user.profile["bio"],
                experiences=list(map(lambda experience: Experience(**experience), user.profile["experiences"])) if user.profile["experiences"] is not None else None,
                certifications=list(map(lambda certificate: Certificate(**certificate), user.profile["certifications"])) if user.profile["certifications"] is not None else None,
                educations=list(map(lambda education: Education(**education), user.profile["educations"])) if user.profile["educations"] is not None else None
        ),
            extras=user.extras,
            is_archived=user.is_archived)
