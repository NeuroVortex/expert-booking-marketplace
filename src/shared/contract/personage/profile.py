from typing import NamedTuple

from .certificate import Certificate
from .education import Education
from .experience import Experience
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
