import loguru
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from apps.notifications.service import smsc_service
from apps.notifications.service import telegram_service


@shared_task
def send_message_task(
        email: str,
        phone_number: str,
        telegram_id: int,
        message: str,
):
    try:
        send_mail(
            'Сообщение от notifications system',
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return 'Письмо успешно отправлено'
    except Exception:
        pass

    try:
        sms_response = smsc_service.send(
            phone=phone_number,
            message=message,
        )
        return 'SMS успешно отправлено'
    except Exception:
        pass

    try:
        telegram_response = telegram_service.send_message(
            chat_id=telegram_id,
            text=message,
        )
        return 'Сообщение в Telegram успешно отправлено'
    except Exception:
        pass


    return 'Ошибка при отправке уведомления'
