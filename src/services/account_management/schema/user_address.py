from sqlalchemy import Column, TIMESTAMP, func, String, BigInteger, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.infrastructure.db_manager.sql_alchemy.base import BaseModel


class UserAddressModel(BaseModel):
    __tablename__ = 'user_payments'
    user_address_id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    user: Mapped["UserModel"] = relationship("UserModel", back_populates="accounts")
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id", ondelete="CASCADE"))
    title = Column(String, nullable=False)
    detail = Column(JSONB, nullable=False)
    creation_datetime = Column(TIMESTAMP, server_default=func.now())
    update_datetime = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
