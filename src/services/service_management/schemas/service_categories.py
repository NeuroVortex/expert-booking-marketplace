from sqlalchemy import Column, TIMESTAMP, func, String

from src.infrastructure.db_manager.sql_alchemy.base import BaseModel


class ServicesCategoryModel(BaseModel):
    __tablename__ = 'service_categories'
    name = Column(String, nullable=False)
    entry_datetime = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
