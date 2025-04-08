from src.schema.extensions.user import ToGetUser
from src.services.service_management.domain.entities.user_service import UserServiceEntity
from src.services.service_management.routers.extensions.service import ToGetService
from src.services.service_management.schemas.responses.user_service import GetUserService, GetUserServices


class ToGetUserService:
    def __rmatmul__(self, user_service: UserServiceEntity):
        return GetUserService(public_id=user_service.public_id,
                              user=user_service.user @ ToGetUser(),
                              service=user_service.service @ ToGetService(),
                              price=str(user_service.detail.price),
                              duration=str(user_service.detail.duration))

class ToGetUserServices:
    def __rmatmul__(self, user_services: list[UserServiceEntity]):
        return GetUserServices(user_services=[user_service @ ToGetUserService() for user_service in user_services])