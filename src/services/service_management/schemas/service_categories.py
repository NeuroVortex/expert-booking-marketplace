from sqlalchemy import Column, TIMESTAMP, func, String, BigInteger, Boolean
from sqlalchemy.orm import relationship

from src.infrastructure.db_manager.sql_alchemy.base import BaseModel


class ServicesCategory(BaseModel):
    __tablename__ = 'service_categories'
    service_category_id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)
    entry_datetime = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    is_active = Column(Boolean, nullable=False, default=True)

    services = relationship("Service", back_populates="service_categories")
