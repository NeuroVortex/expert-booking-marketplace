import uuid

from sqlalchemy import Column, TIMESTAMP, func, ForeignKey, BigInteger, UUID
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.infrastructure.db_manager.sql_alchemy.base import BaseModel
from src.services.account_management.models.user import User
from src.services.service_management.models.services import Service


class UserService(BaseModel):
    __tablename__ = 'user_services'
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    public_id = Column(UUID(as_uuid=False), unique=True, nullable=False, default=uuid.uuid4)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    service_id: Mapped[int] = mapped_column(ForeignKey(Service.id, ondelete="CASCADE"))
    details = Column(JSONB, nullable=False)
    creation_datetime = Column(TIMESTAMP, server_default=func.now())
    user: Mapped["User"] = relationship("User", back_populates="user_services")
    service: Mapped["Service"] = relationship("Service", back_populates="user_services")
