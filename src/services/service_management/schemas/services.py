import uuid
from typing import List
from uuid import UUID

from sqlalchemy import Column, BigInteger, TIMESTAMP, func, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db_manager.sql_alchemy.base import BaseModel
from src.shared.contract.service.service import Service


class ServiceSchema(BaseModel):
    __tablename__ = 'services'
    service_id = Column(BigInteger, primary_key=True, autoincrement=True)
    parent_service_id = Column(BigInteger, ForeignKey("services.service_id"), nullable=True)
    name: Mapped[str] = mapped_column(nullable=False)
    profile =  Column(JSONB, nullable=False)
    details =  Column(JSONB, nullable=False)
    identifier: Mapped[str] = mapped_column(default=uuid.uuid4(), nullable=False)
    creation_datetime = Column(TIMESTAMP, nullable=False, server_default=func.now())
    update_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    is_active: Mapped[bool] = mapped_column(nullable=False, default=True)

    user_services = relationship("UserService", back_populates="services")
    parent_service: Mapped["Service"] = relationship("Service", remote_side=[service_id], back_populates="children")
    children: Mapped[List["Service"]] = relationship("Service", back_populates="parent_service", cascade="all, delete")

