import json


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
            settings.SMSC_SEND_API_URL,
            params=params
        )

        return response


class TelegramService:
    def __init__(
            self,
            bot_token: str = settings.BOT_TOKEN,
            api_url: str = settings.TELEGRAM_API_URL
    ):
        self.__bot_token = bot_token
        self.api_url = api_url

    @property
    def __bot_api_url(self):
        return f'{self.api_url}/bot{self.__bot_token}'

    def send_message(
            self,
            chat_id: int,
            text: str,
            reply_markup: dict[str, list] | None = None,
            parse_mode: str = 'HTML',
    ):
        headers = {'Content-Type': 'application/json'}
        payload = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': parse_mode,
        }

        if reply_markup:
            payload['reply_markup'] = json.dumps(reply_markup)

        response = requests.post(
            url=f'{self.__bot_api_url}/sendMessage',
            data=json.dumps(payload),
            headers=headers
        )

        return response


telegram_service = TelegramService()
smsc_service = SMSCService()
