from src.Application.AppSetting import AppSetting


def app_selector():
    match str(AppSetting.APP_SETTINGS['appConfig']['app']).lower():
        case _:
            pass