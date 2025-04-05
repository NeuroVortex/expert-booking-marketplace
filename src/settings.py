import logging
from decimal import ROUND_DOWN

from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

from src.app.app_settings import AppSettings
from src.app.config import Router
from src.app.router.app import app_router
from src.services.account_management.infrastructure.models.account import Account
from src.services.account_management.infrastructure.models.user import User
from src.services.account_management.infrastructure.models.user_address import UserAddress
from src.services.account_management.infrastructure.models.user_payment import UserPayment
from src.services.account_management.routers.users import user_router
from src.services.booking.routers.appointment_routers import appointment_router

from src.services.booking.models.reservation import Reservation
from src.services.service_management.routers.service import service_router
from src.services.service_management.infrastructure.models.services import Service
from src.services.service_management.infrastructure.models.user_services import UserService
from src.services.service_management.routers.user_service import user_service_router

AppSettings()
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
    User,
    UserPayment,
    UserAddress,
    Reservation,
    Account,
    Service,
    UserService
]

Routers = [
    Router(prefix="", router=app_router, tags=["/"]),
    Router(prefix='/v1/services', router=service_router, tags=["services"]),
    Router(prefix='/v1/users', router=user_router, tags=["users"]),
    Router(prefix='/v1/user_services', router=user_service_router, tags=["user-services"]),
    Router(prefix='/v1/appointments', router=appointment_router, tags=["reservation"]),
]

EXECUTORS = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(5)
}
JOB_DEFAULTS = {
    'coalesce': AppSettings.APP_SETTINGS["timerConfig"]["coalesce"],
    'max_instances': AppSettings.APP_SETTINGS["timerConfig"]["max_instances"],
}


logging.getLogger('apscheduler.executors.default').propagate = False

DECIMAL_PRECISION = AppSettings.APP_SETTINGS["businessConfig"]["accuracy"]["decimalPrecision"]
DECIMAL_ROUNDING = ROUND_DOWN