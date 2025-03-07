from typing import NamedTuple

from src.shared.contract.personage.gender import Gender
from src.shared.contract.personage.profile import Profile


class User(NamedTuple):
    user_id: str
    first_name: str
    last_name: str
    phone: str
    email: str
    gender: Gender
    identifier: str
    profile: Profile
    extras: dict | None = None
    is_archived: bool = False
