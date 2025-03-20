from typing import NamedTuple

from src.services.account_management.domain.providers.certificate import Certificate
from src.services.account_management.domain.providers.education import Education
from src.services.account_management.domain.providers.experience import Experience
from .location import Location


class Profile(NamedTuple):
    name: str
    photo_path: str
    headline: str
    website: str
    location: Location
    years_of_experience: int
    bio: str
    experiences: list[Experience] | None = None
    certifications: list[Certificate] | None = None
    educations: list[Education] | None = None
