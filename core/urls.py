from django.urls import path
from .views import *

urlpatterns = [
    # list items endpoints
    path('news/get/', ListNewsItemView.as_view()),
    path('tag/get/', ListTagView.as_view()),
    # create endpoints
    path('news/create/', CreateNewsItemView.as_view()),
    path('tag/create/', CreateTagView.as_view()),
    path('comment/<id>/create/', AddComments.as_view()),
    # get details/delete item endpoints
    path('news/get/<str:id>/', NewsItemDetailView.as_view()),
    path('news/get/<str:id>/comments/', GetComments.as_view()),
    # search views
    path('tag/search/', TagSearchView.as_view()),
    path('news/search/', NewsSearchView.as_view()),
    # like/dislike news views
    path('news/<str:id>/like/', LikeNewsView.as_view()),
    path('news/<str:id>/dislike/', DislikeNewsView.as_view()),
]