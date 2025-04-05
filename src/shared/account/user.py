from typing import NamedTuple

from src.services.account_management.domain.providers.gender import Gender
from src.services.account_management.domain.profile import Profile


class UserEntity(NamedTuple):
    id: int | None
    user_public_id: str | None
    first_name: str
    last_name: str
    phone: str
    email: str
    gender: Gender
    identifier: str
    profile: Profile
    extras: dict | None = None
    is_archived: bool = False
