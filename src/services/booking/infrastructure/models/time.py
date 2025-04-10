import uuid

from sqlalchemy import Column, String, BigInteger, ForeignKey, UUID, Date, Time, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.testing.schema import mapped_column

from src.infrastructure.db_manager.sql_alchemy.base import BaseModel
from src.services.account_management.infrastructure.models.user import User


class TimeSlot(BaseModel):
    __tablename__ = "time_slots"
    id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True, nullable=False, index=True)
    public_id = Column(UUID(as_uuid=False), primary_key=True, index=True, unique=True, default=uuid.uuid4, nullable=False)
    user_id = mapped_column(ForeignKey(User.id, ondelete="CASCADE"), nullable=False)
    date = Column(Date, index=True)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    period = Column(String, nullable=False)  # Morning / Afternoon / Evening
    is_booked = Column(Boolean, nullable=False, default=False)

    reservation = relationship("Reservation", back_populates="time_slot")
    user = relationship(User, back_populates="time_slots")