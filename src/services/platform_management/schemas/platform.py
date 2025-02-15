from sqlalchemy import Column, TIMESTAMP, func, String, BigInteger, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.infrastructure.db_manager.sql_alchemy.base import BaseModel


class UserPlatformModel(BaseModel):
    __tablename__ = 'user_platforms'
    user_platform_id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    user: Mapped["UserModel"] = relationship("UserModel", back_populates="accounts")
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id", ondelete="CASCADE"))
    platform_type = Column(String, nullable=False)
    platform_detail = Column(JSONB, nullable=False)
    registration_datetime = Column(TIMESTAMP, server_default=func.now())
    update_datetime = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
