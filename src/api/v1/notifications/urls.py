from django.urls import path
from api.v1.notifications import views

urlpatterns = [
    path(
        'send/',
        views.SendNotificationView.as_view(),
        name='send_notification'
    ),
]
