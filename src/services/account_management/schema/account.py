from sqlalchemy import Column, TIMESTAMP, func, String, BigInteger, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.infrastructure.db_manager.sql_alchemy.base import BaseModel
from src.services.account_management.schema.user import User


class Account(BaseModel):
    __tablename__ = 'accounts'
    account_id = Column(UUID, primary_key=True, autoincrement=True, nullable=False)
    user_id = mapped_column(BigInteger, ForeignKey(User.user_id, ondelete="CASCADE"))
    platform_type = Column(String, nullable=False)
    username = Column(String, nullable=False)
    authentication = Column(JSONB, nullable=False)
    detail = Column(JSONB, nullable=True)
    is_archived = Column(Boolean, nullable=False, default=False)
    creation_datetime = Column(TIMESTAMP, server_default=func.now())
    update_datetime = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())

    user: Mapped["User"] = relationship(User, back_populates="accounts")
