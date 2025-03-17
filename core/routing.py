# routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/likes_dislikes/<str:id>/', consumers.LikesDislikesConsumer.as_asgi()),
]