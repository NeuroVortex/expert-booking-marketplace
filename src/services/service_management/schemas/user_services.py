from sqlalchemy import Column, TIMESTAMP, func, ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.infrastructure.db_manager.sql_alchemy.base import BaseModel
from src.services.account_management.schema.user import User
from src.services.service_management.schemas.services import Service


class UserService(BaseModel):
    __tablename__ = 'user_services'
    user_Service_id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.user_id, ondelete="CASCADE"))
    service_id: Mapped[int] = mapped_column(ForeignKey(Service.service_id, ondelete="CASCADE"))
    creation_datetime = Column(TIMESTAMP, server_default=func.now())

    user: Mapped["User"] = relationship("User", back_populates="user_services")
    service: Mapped["Service"] = relationship("Service", back_populates="user_services")
