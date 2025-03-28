from src.services.service_management.domain.entities.user_service import UserServiceEntity
from src.services.service_management.infrastructure.models.user_services import UserService


class UserServicesToModel:
    def __rmatmul__(self, user_service: UserServiceEntity):
        return UserService(user_id=user_service.user.id,
                           service_id=user_service.service.id,
                           details=user_service.detail._asdict())