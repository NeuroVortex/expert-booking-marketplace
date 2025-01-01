import logging
from decimal import ROUND_DOWN
from sys import prefix

from fastapi.middleware.cors import CORSMiddleware
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

from src.application.app_settings import AppSetting
from src.app.config import Router
from src.app.router.app import app_router
from src.services.crm.routers.appointment_routers import appointment_router
from src.services.sales.routers.service import service_router

AppSetting()
Allowed_Origins = [
    "http://localhost.com",
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:5173"
]
Allow_Credentials = True
Allowed_Methods = ["*"]
Allowed_Headers = ["*"]

Registered_Models = [
    # TraderModel,
    # Task,
    # TaskContainer,
    # SimilarStock
]

Routers = [
    Router(prefix="", router=app_router, tags=["/"]),
    Router(prefix='/v1/services', router=service_router, tags=["Service"]),
    Router(prefix='/v1/appointments', router=appointment_router, tags=["AppointmentModel"]),
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