from django.urls import path, re_path

from .views import *




urlpatterns = [
    path('', TweetListView.as_view(), name='list_view'),
    path('<int:pk>/',  TweetDetailView.as_view(), name='detail_view'),
]