from django.urls import path

from . import views

app_name = 'stocks'

urlpatterns = [
    path('', views.StockList.as_view(), name='all'),
    path('new/', views.CreateStock.as_view(), name='create'),
    path('by/<str:username>/', views.UserStocks.as_view(), name='for_user'),
    path('delete/<int:pk>/', views.DeleteStock.as_view(), name='delete')
]