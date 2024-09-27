from django.urls import path
from notices.views import home

urlpatterns = [
    path('', home),
]
