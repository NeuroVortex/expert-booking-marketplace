import uuid

from sqlalchemy import Column, TIMESTAMP, func, String, BigInteger, ForeignKey, UUID
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.infrastructure.db_manager.sql_alchemy.base import BaseModel
from src.services.account_management.infrastructure.models.user import User
from src.services.account_management.infrastructure.models.user_address import UserAddress


class Reservation(BaseModel):
    __tablename__ = 'reservations'
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False, index=True)
    public_id = Column(UUID(as_uuid=False), primary_key=True, unique=True, default=uuid.uuid4, nullable=False, index=True)
    user_address_id: Mapped[int] = mapped_column(ForeignKey(UserAddress.id, ondelete="CASCADE"))
    service_provider_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    state = Column(String, nullable=False)
    detail = Column(JSONB, nullable=False)
    procedure = Column(JSONB, nullable=False)
    feedback = Column(JSONB, nullable=False)
    history = Column(JSONB, nullable=False)
    creation_datetime = Column(TIMESTAMP, server_default=func.now())
    update_datetime = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    user_addresses: Mapped["UserAddress"] = relationship("UserAddress", back_populates="reservations")
    service_provider: Mapped["User"] = relationship("User", back_populates="reservations")
