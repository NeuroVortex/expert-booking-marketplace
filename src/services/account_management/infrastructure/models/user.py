import uuid

from sqlalchemy import Column, TIMESTAMP, func, String, BigInteger, Boolean, UUID
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from src.infrastructure.db_manager.sql_alchemy.base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
    public_id = Column(UUID(as_uuid=True), unique=True, primary_key=True, nullable=False, default=uuid.uuid4, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    primary_email = Column(String, nullable=False)
    primary_phone = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    identifier = Column(String, nullable=False)
    profile = Column(JSONB, nullable=False)
    extras = Column(JSONB, nullable=True)
    is_archived = Column(Boolean, nullable=False, default=False)
    registration_datetime = Column(TIMESTAMP, server_default=func.now())
    update_datetime = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())

    accounts = relationship("Account", back_populates='user')
    user_payments = relationship("UserPayment", back_populates='user')
    user_services = relationship("UserService", back_populates='user')
    user_addresses = relationship("UserAddress", back_populates='user')
    reservations = relationship("Reservation", back_populates='service_provider')
