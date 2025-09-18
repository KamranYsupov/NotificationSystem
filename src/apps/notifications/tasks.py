import loguru
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from src.apps.notifications.service import smsc_service

@shared_task
def send_message_task(
        email: str,
        phone_number: str,
        message: str,
):
    try:
        send_mail(
            'Сообщение от notifications system',
            message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        return 'Email успешно отправлено'
    except Exception as e:
        loguru.logger.error(f'Ошибка при отправке email: {e}')

    sms_response = smsc_service.send(
        phone=phone_number,
        message=message,
    )
    if sms_response.ok:
        return 'SMS sent successfully'
    else:
        sms_response_json = sms_response.json()
        sms_error = sms_response_json['result']['error']
        loguru.logger.error(f'Ошибка при отправке sms: {sms_error}')


    return 'Failed to send both email and SMS'
