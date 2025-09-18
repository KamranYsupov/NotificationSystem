import requests
from django.conf import settings


class SMSCService:
    def __init__(
            self,
            login: str = settings.SMSC_LOGIN,
            psw: str = settings.SMSC_PASSWORD,
    ):
        self.login = login
        self.__psw = psw

    def send(
            self,
            phone: str,
            message: str,
            seconds_to_wait: int = 25,
            repeat_interval: int = 0,
            attemps_count: int = 1,
            call: bool = False,
    ):
        params = {
            'login': self.login,
            'psw': self.__psw,
            'phones': phone,
            'mes': message,
            'call': int(call),
            'param': (
                f'{seconds_to_wait},{repeat_interval},{attemps_count}'
            )
        }

        response = requests.get(
            settings.SMSC_CREATE_CALL_URL,
            params=params
        )

        return response


smsc_service = SMSCService()
