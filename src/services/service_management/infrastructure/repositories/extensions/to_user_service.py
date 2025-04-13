from src.services.account_management.infrastructure.repositories.extensions.user import ToUser
from src.services.service_management.domain.entities.user_service import UserServiceEntity
from src.services.service_management.domain.value_objects.user_service_detail import UserServiceDetail
from src.services.service_management.infrastructure.models.user_services import UserService
from src.services.service_management.infrastructure.repositories.extensions.to_service import ModelToServiceEntity



class ModelToUserServiceEntity:
    def __rmatmul__(self, user_service: UserService):
        return UserServiceEntity(
            user=user_service.user @ ToUser(),
            service=user_service.service @ ModelToServiceEntity(),
            detail=UserServiceDetail.from_dict(user_service.details),
            id=user_service.id,
            public_id=user_service.public_id
        )
