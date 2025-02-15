from sqlalchemy import Column, BigInteger, TIMESTAMP, func, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db_manager.sql_alchemy.base import BaseModel


class ServiceModel(BaseModel):
    __tablename__ = 'services'
    service_id = Column(BigInteger, primary_key=True, autoincrement=True)
    service_category: Mapped["ServiceCategories"] = relationship("ServiceCategoryModel", back_populates="services")
    service_category_id: Mapped[int] = mapped_column(ForeignKey("service_category.service_category_id"))
    name = Column(String, nullable=False)
    detail = Column(JSONB, nullable=False)
    creation_datetime = Column(TIMESTAMP, nullable=False, server_default=func.now())
    update_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
