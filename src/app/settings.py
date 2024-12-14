import logging
from decimal import ROUND_DOWN

from src.application.app_settings import AppSetting
from src.app.config import Router
from src.app.router.app import app_router
from fastapi.middleware.cors import CORSMiddleware


Middleware=[
    CORSMiddleware
]
AllowOrigins = ["*"]
AllowMethods = ["*"]
AllowHeaders = ["*"]

Registered_Models = [
    # TraderModel,
    # Task,
    # TaskContainer,
    # SimilarStock
]

Routers = [
    Router(prefix="", router=app_router, tags=["/"]),
    Router(prefix='/v1/appointment', router=add_trader_router, tags=["Personage"]),
    Router(prefix='/v1/service', router=get_traders_router, tags=["Personage"]),
]

logging.getLogger('apscheduler.executors.default').propagate = False

DECIMAL_PRECISION = AppSetting.APP_SETTINGS["businessConfig"]["accuracy"]["decimalPrecision"]
DECIMAL_ROUNDING = ROUND_DOWN