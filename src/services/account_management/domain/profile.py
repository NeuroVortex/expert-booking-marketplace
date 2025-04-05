from typing import NamedTuple

from src.services.account_management.domain.providers.certificate import Certificate
from src.services.account_management.domain.providers.education import Education
from src.services.account_management.domain.providers.experience import Experience
from .location import Location


class Profile(NamedTuple):
    name: str
    location: Location
    photo_path: str | None = None
    headline: str | None = None
    website: str | None = None
    years_of_experience: int | None = None
    bio: str | None = None
    experiences: list[Experience] | None = None
    certifications: list[Certificate] | None = None
    educations: list[Education] | None = None
