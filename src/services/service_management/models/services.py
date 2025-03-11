import uuid
from typing import List

from sqlalchemy import Column, BigInteger, TIMESTAMP, func, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db_manager.sql_alchemy.base import BaseModel


class Service(BaseModel):
    __tablename__ = 'services'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    public_id = Column(UUID(as_uuid=False), unique=True, nullable=False, default=uuid.uuid4)
    parent_service_id = Column(BigInteger, ForeignKey("services.id"), nullable=True)
    name: Mapped[str] = mapped_column(nullable=False)
    profile =  Column(JSONB, nullable=False)
    details =  Column(JSONB, nullable=False)
    creation_datetime = Column(TIMESTAMP, nullable=False, server_default=func.now())
    update_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    is_active: Mapped[bool] = mapped_column(nullable=False, default=True)

    user_services = relationship("UserService", back_populates="service")
    parent: Mapped["Service"] = relationship("Service", remote_side=[id], back_populates="children")
    children: Mapped[List["Service"]] = relationship("Service", back_populates="parent", cascade="all, delete")

