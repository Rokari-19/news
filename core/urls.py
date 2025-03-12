from django.urls import path
from .views import *

urlpatterns = [
    # retreive endpoints
    path('news/get/', LlistNewsItemView.as_view()),
    path('tag/get/', ListTagView.as_view()),
]