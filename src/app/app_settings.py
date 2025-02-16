import json
import os
from pathlib import Path


class AppSettings(object):
    APP_SETTINGS: dict = {}
    CREDENTIALS: dict = {}

    def __init__(self):
        self.__file_format = ".json"
        self.__evaluate_settings()

    def __evaluate_settings(self):
        match str(os.getenv("MODE", 'dev')).upper():
            case "PROD" | "PRODUCTION":
                app_settings = "app-settings"
                credential = 'credentials'

            case "STG" | "STAGE":
                app_settings = "app-settings-stg"
                credential = 'credentials-stg'

            case _:
                app_settings = "app-settings-dev"
                credential = 'credentials-dev'

        credential = str(os.getenv("CREDENTIAL_NAME", credential))
        self.__read(app_settings, credential)

    def __read(self, app_settings_file, credential_file):
        app_setting_path = os.path.join(Path(__file__).resolve().parent, app_settings_file + self.__file_format)
        credentials_path = os.path.join(Path(__file__).resolve().parent, credential_file + self.__file_format)

        with open(app_setting_path, "r") as f:
            AppSettings.APP_SETTINGS = json.load(f)

        with open(credentials_path, "r") as f:
            AppSettings.CREDENTIALS = json.load(f)
