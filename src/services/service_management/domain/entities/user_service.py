from dataclasses import dataclass

from src.shared.account.user import UserEntity
from src.services.service_management.domain.entities.service import ServiceEntity
from src.services.service_management.domain.value_objects.user_service_detail import UserServiceDetail


@dataclass
class UserServiceEntity:
    user: UserEntity
    service: ServiceEntity
    detail: UserServiceDetail
    id: int | None = None
