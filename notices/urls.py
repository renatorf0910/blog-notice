from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('notices/<int:id>/', views.notice_details),
]
