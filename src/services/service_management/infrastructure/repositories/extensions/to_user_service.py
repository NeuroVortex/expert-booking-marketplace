from src.services.service_management.domain.entities.user_service import UserServiceEntity
from src.services.service_management.infrastructure.models.user_services import UserService
from src.services.service_management.application.extensions.service import DtoToServiceEntity


class EntityToUserServiceDAO:
    def __rmatmul__(self, user_service: UserServiceEntity):
        return UserService(
            user_id = user_service.user.user_id,
            service_id = user_service.service.id,
            details = user_service.detail._asdict()
        )


class ModelToUserServiceEntity:
    def __rmatmul__(self, user_service: UserService):
        user = user_service.user @ ToUserEntity()
        service = user_service.service @ DtoToServiceEntity()

        return UserServiceEntity(

        )
