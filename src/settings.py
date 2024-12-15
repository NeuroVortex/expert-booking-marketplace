import logging
from decimal import ROUND_DOWN
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

from src.application.app_settings import AppSetting
from src.app.config import Router
from src.app.router.app import app_router
from src.services.sales.routers.service import service_router

Middleware=CORSMiddleware
Middleware_rules = {
    "allow_origins": ["*"],
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}

Registered_Models = [
    # TraderModel,
    # Task,
    # TaskContainer,
    # SimilarStock
]

Routers = [
    Router(prefix="", router=app_router, tags=["/"]),
    Router(prefix='/v1/services', router=service_router, tags=["Service"]),
]

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