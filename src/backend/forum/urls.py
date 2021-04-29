from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.ForumListView.as_view()),
    #path('<int:user_id>/', views.UserLoginHistoryListView.as_view()),
    #path('myhistory/', views.MyLoginHistoryListView.as_view())
]
