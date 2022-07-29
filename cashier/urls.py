from django.urls import path, include
from . import views

urlpatterns = [
    path('cashier1/', views.cashier1, name='cashier1'),
    path('cashier2/', views.cashier2, name='cashier2'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('add_money', views.add_money, name='add_money')
]