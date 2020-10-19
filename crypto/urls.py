from django.urls import path

from . import views

app_name = 'crypto'

urlpatterns = [
    path('', views.CryptoList.as_view(), name='list')
]