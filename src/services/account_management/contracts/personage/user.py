from typing import NamedTuple

from src.services.account_management.contracts.personage.gender import Gender
from src.services.account_management.contracts.personage.profile import Profile


class User(NamedTuple):
    first_name: str
    last_name: str
    phone: str
    email: str
    gender: Gender
    identifier: str
    profile: Profile
    user_id: str | None = None
    extras: dict | None = None
    is_archived: bool = False
