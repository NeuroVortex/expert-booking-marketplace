from sqlalchemy import Column, JSON, String, BigInteger, BOOLEAN, TIMESTAMP
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func

from src.infrastructure.db_manager.sql_alchemy.base import BaseModel
from src.services.crm.contract.client import Client


class UserModel(BaseModel):
    __tablename__ = 'client'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    identifier = Column(String, nullable=False)
    profile = Column(String, nullable=False)
    user_type = Column(String, nullable=True)
    is_blocked = Column(BOOLEAN, default=False)
    last_update_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())

    @classmethod
    def to_model(cls, client: Client):
        profile = {
            "first_name":client.first_name,
            "last_name": client.last_name,
            "phone": client.phone,
            "email": client.email
        }
        return cls(identifier=client.identifier,
                   profile=profile,
                   user_type=trader.identity_info.to_db(),
                   client_type=trader.parent_identifier,
                   user_type=trader.user_type.name,
                   trader_type=trader.trader_type.name,
                   use_shadow=trader.shadow,
                   is_active=trader.is_active)

    def to_trader(self) -> TraderInfo:
        return TraderInfo(db_id=self.id,
                          trader_identifier=self.trader_identifier,
                          identity_info=IdentityInfo.to_identity(self.identity_info),
                          is_active=self.is_active,
                          user_identifier=self.user_identifier,
                          parent_identifier=self.parent_identifier,
                          shadow=self.use_shadow,
                          user_type=UserType[self.user_type],
                          trader_type=TraderTypeDto[self.trader_type])
