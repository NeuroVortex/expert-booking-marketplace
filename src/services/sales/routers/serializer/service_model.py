from pydantic import BaseModel, Field, ConfigDict

from common.Contract.Personage.Dto.TraderTypeDto import TraderTypeDto
from src.Domain.Contract.Personage import UserType
from src.Services.CopyService.routers.Serializer.TraderTypeModel import TraderTypeModel
from src.Services.CopyService.routers.Serializer.UserTypeModel import UserTypeModel
from src.Services.CopyService.schema.Personage.AddTraderDto import AddTraderDto


class ServiceModel(BaseModel):
    UserId: str
    BourseCodeId: str
    MasterBourseCodeId: str | None = Field(None,
                                           example=None,
                                           description="Bourse code ID for the parent trader")
    UserType: UserTypeModel
    TraderType: TraderTypeModel = TraderTypeModel.CustomerTrader
    Shadow: bool | None = False
    IP: str | None = None
    Source: str | None = None

    def to_dto(self) -> AddTraderDto:
        return AddTraderDto(user_id=self.UserId,
                            bourse_code_id=self.BourseCodeId,
                            master_bourse_code_id=self.MasterBourseCodeId,
                            shadow=self.Shadow,
                            ip=None,
                            source=None,
                            user_type=UserType[self.UserType.name],
                            trader_type=TraderTypeDto[self.TraderType.name])