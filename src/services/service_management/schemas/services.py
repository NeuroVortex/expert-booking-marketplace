from sqlalchemy import Column, BigInteger, TIMESTAMP, func, ForeignKey, String, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db_manager.sql_alchemy.base import BaseModel
from src.services.service_management.schemas.service_categories import ServicesCategory


class Service(BaseModel):
    __tablename__ = 'services'
    service_id = Column(BigInteger, primary_key=True, autoincrement=True)
    service_category_id = mapped_column(BigInteger, ForeignKey(ServicesCategory.service_category_id))
    name = Column(String, nullable=False)
    detail = Column(JSONB, nullable=False)
    creation_datetime = Column(TIMESTAMP, nullable=False, server_default=func.now())
    update_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    is_active = Column(Boolean, nullable=False, default=True)

    user_services = relationship("UserService", back_populates="services")
    service_category: Mapped["ServicesCategory"] = relationship("ServiceCategory", back_populates="services")
