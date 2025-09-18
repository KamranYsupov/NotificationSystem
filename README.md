<h2>🚀 Установка и запуск</h2>


<h4>
1. Создайте файл .env в корневой директории согласно .env.example
</h4>

```requirements
PROJECT_NAME=
SECRET_KEY=
DEBUG=

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=db
DB_PORT=5432

REDIS_HOST=redis
REDIS_PORT=6379

BOT_TOKEN=

SMSC_LOGIN=
SMSC_PASSWORD=

EMAIL_HOST=
EMAIL_PORT=
EMAIL_USE_TLS=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

<h4>
2. Запустите docker compose:
</h4>

```commandline
docker compose up --build -d
```

<h4>Пример запроса для отправки уведомления:</h4>

```commandline
curl -X POST http://127.0.0.1/api/v1/notifications/send/ 
-H "Content-Type: application/json" 
-d '{"message": "message", email": "example@example.com", "phone_number": "+79999999999", "telegram_id": 2312323}'
```
_Сообщения в Telegram не будут приходить, пока бот не активирован командой /start._

_Сервис smsc.ru в тестовом режиме отправляет сообщения только абонентам Билайн и Теле2 и пропускает только сообщения типа "Тест"._