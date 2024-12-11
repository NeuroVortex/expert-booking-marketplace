import logging
from decimal import ROUND_DOWN

from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

from src.Application.AppSetting import AppSetting
from src.Services.CopyService.models.TraderModel import TraderModel
from src.Services.ExecutionService.model import Task, TaskContainer
from src.Services.CopyService.routers.Personage.AddTrader import add_trader_router
from src.Services.CopyService.routers.Personage.GetTraders import get_traders_router
from src.Services.SimilarStockDetectorService.model.SimilarStock import SimilarStock
from src.app.Config import Router
from src.app.router.app import app_router


Registered_Models = [
    TraderModel,
    Task,
    TaskContainer,
    SimilarStock
]

Routers = [
    Router(prefix="", router=app_router, tags=["/"]),
    Router(prefix='/v1/personage', router=add_trader_router, tags=["Personage"]),
    Router(prefix='/v1/personage', router=get_traders_router, tags=["Personage"]),
]

TIME_ZONE = 'Asia/Tehran'

EXECUTORS = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(5)
}
JOB_DEFAULTS = {
    'coalesce': AppSetting.APP_SETTINGS["timerConfig"]["coalesce"],
    'max_instances': AppSetting.APP_SETTINGS["timerConfig"]["max_instances"],
}

logging.getLogger('apscheduler.executors.default').propagate = False

DECIMAL_PRECISION = AppSetting.APP_SETTINGS["businessConfig"]["accuracy"]["decimalPrecision"]
DECIMAL_ROUNDING = ROUND_DOWN