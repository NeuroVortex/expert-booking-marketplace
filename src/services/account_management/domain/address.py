from dataclasses import dataclass

from src.shared.account.user import UserEntity


@dataclass
class AddressEntity:
    id: int
    public_id: str
    user: UserEntity
    province: str
    city: str
    homeNumber: str
    firstLineAddress: str
    secondLineAddress: str | None
    zipCode: str
