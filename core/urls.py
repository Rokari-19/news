from django.urls import path
from .views import *

urlpatterns = [
    # list items endpoints
    path('news/get/', ListNewsItemView.as_view()),
    path('tag/get/', ListTagView.as_view()),
    # create endpoints
    path('news/create/', CreateNewsItemView.as_view()),
    path('tag/create/', CreateTagView.as_view()),
    # get details endpoints
    path('news/get/<str:id>/', NewsItemDetailView.as_view()),
    # delete endpoints
]