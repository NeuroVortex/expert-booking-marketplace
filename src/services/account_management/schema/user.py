from sqlalchemy import Column, TIMESTAMP, func, String, BigInteger
from sqlalchemy.dialects.postgresql import JSONB

from src.infrastructure.db_manager.sql_alchemy.base import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    primary_email = Column(String, nullable=False)
    primary_phone = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    identifier = Column(String, nullable=False)
    profile = Column(JSONB, nullable=False)
    extra = Column(JSONB, nullable=True)
    registration_datetime = Column(TIMESTAMP, server_default=func.now())
    update_datetime = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
