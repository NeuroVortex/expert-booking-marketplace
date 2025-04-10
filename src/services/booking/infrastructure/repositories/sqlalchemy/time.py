from sqlalchemy.orm import Session
from src.services.booking.domain.time import TimeSlotEntity
from src.services.booking.domain.period import TimePeriod
from src.services.account_management.infrastructure.models.user import User
from src.services.booking.infrastructure.models.time_slot import TimeSlot
from src.shared.account.user import UserEntity
from src.services.booking.infrastructure.repositories.time_slot_repository import TimeSlotRepository


class TimeSlotRepositoryImpl(TimeSlotRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_slot(self, time_slot: TimeSlotEntity) -> TimeSlotEntity:
        db_slot = TimeSlot(
            date=time_slot.date,
            start_time=time_slot.start_time,
            end_time=time_slot.end_time,
            period=time_slot.period.value,
            is_booked=time_slot.is_booked,
        )
        self.db.add(db_slot)
        self.db.commit()
        self.db.refresh(db_slot)

        return TimeSlotEntity(
            id=db_slot.id,
            public_id=str(db_slot.public_id),
            date=db_slot.date,
            start_time=db_slot.start_time,
            end_time=db_slot.end_time,
            period=TimePeriod(db_slot.period),
            is_booked=db_slot.is_booked
        )

    def delete(self, time_slot: TimeSlotEntity) -> None:
        db_slot = self.db.query(TimeSlot).filter(TimeSlot.public_id == time_slot.public_id).first()
        if db_slot:
            self.db.delete(db_slot)
            self.db.commit()

    def get_slots_by_user(self, user: UserEntity) -> list[TimeSlotEntity]:
        slots = (
            self.db.query(TimeSlot)
            .filter(TimeSlot.user_id == user.id)
            .order_by(TimeSlot.date, TimeSlot.start_time)
            .all()
        )

        return [
            TimeSlotEntity(
                id=slot.id,
                public_id=str(slot.public_id),
                date=slot.date,
                start_time=slot.start_time,
                end_time=slot.end_time,
                period=TimePeriod(slot.period),
                is_booked=slot.is_booked
            )
            for slot in slots
        ]

    def booked(self, time_slot_public_id: str):
        db_slot = self.db.query(TimeSlot).filter(TimeSlot.public_id == time_slot_public_id).first()
        if db_slot:
            db_slot.is_booked = True
            self.db.commit()