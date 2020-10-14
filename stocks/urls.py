from django.urls import path

from . import views

app_name = 'stocks'

urlpatterns = [
    path('new/', views.CreateStock.as_view(), name='create'),
    path('by/<str:username>/', views.UserStocks.as_view(), name='for_user'),
    path('by/<str:username>/<int:pk>/', views.StockDetail.as_view(), name='single'),
    path('delete/<int:pk>/', views.DeleteStock.as_view(), name='delete'),
]