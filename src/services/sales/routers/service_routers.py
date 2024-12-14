from fastapi import APIRouter, Depends, HTTPException, status

add_service_router = APIRouter()


@add_service_router.post(path="/service", tags=["service"], status_code=status.HTTP_200_OK)
async def add_trader(trader_model: TraderModel) -> AddTraderResponse:
    try:
        trader_dto = trader_model.to_dto()

        is_exist = await algorithm_handler.is_exist(identity=trader_dto.bourse_code_id)

        if not is_exist:
            identity_info: IdentityInfo = await personage_handler.get_personage(str(trader_dto.bourse_code_id),
                                                                                IdentityTypeDto.BourseCodeId)
            trader = TraderInfo(db_id=None,
                                identity_info=identity_info,
                                user_identifier=trader_dto.user_id,
                                trader_identifier=trader_dto.bourse_code_id,
                                parent_identifier=trader_dto.master_bourse_code_id,
                                shadow=trader_dto.shadow,
                                user_type=trader_dto.user_type,
                                trader_type=trader_dto.trader_type,
                                is_active=True)
            await algorithm_handler.add_trader(trader)
            ActorSystem.actor_ref.tell(AlgorithmUpdateRequest())

            return AddTraderResponse(traderId=trader.db_id, message='create trader successfully')

        else:
            return AddTraderResponse(traderId=0, message='Trader already exist')

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))