from .views import InicialView
from django.urls import path

urlpatterns = [
    path('', InicialView.as_view(), name='inicial'),
]
