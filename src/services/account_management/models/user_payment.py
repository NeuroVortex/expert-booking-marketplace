import uuid

from sqlalchemy import Column, TIMESTAMP, func, String, BigInteger, ForeignKey, Boolean, UUID
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.infrastructure.db_manager.sql_alchemy.base import BaseModel
from .user import User


class UserPayment(BaseModel):
    __tablename__ = 'user_payments'
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    ref_id = Column(UUID(as_uuid=True), unique=True, primary_key=True, nullable=False, default=uuid.uuid4)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    payment_method = Column(String, nullable=False)
    is_archived = Column(Boolean, nullable=False, default=False)
    creation_datetime = Column(TIMESTAMP, server_default=func.now())
    update_datetime = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    user: Mapped["User"] = relationship("User", back_populates="user_payments")
