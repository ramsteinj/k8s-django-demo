from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    #path('', views.YogiyoUserView.as_view()),
    path('<int:id>/', views.YogiyoUserView.as_view()),
]
