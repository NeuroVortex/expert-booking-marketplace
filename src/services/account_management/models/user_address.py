import uuid

from sqlalchemy import Column, TIMESTAMP, func, String, BigInteger, ForeignKey, Boolean, UUID
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.infrastructure.db_manager.sql_alchemy.base import BaseModel
from .user import User


class UserAddress(BaseModel):
    __tablename__ = 'user_addresses'
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    public_id = Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid.uuid4)
    user_id = mapped_column(BigInteger, ForeignKey(User.id, ondelete="CASCADE"))
    title = Column(String, nullable=False)
    detail = Column(JSONB, nullable=False)
    is_archived = Column(Boolean, nullable=False, default=False)
    creation_datetime = Column(TIMESTAMP, server_default=func.now())
    update_datetime = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())

    reservations = relationship("Reservation", back_populates="user_addresses")
    user: Mapped["User"] = relationship("User", back_populates="user_addresses")
