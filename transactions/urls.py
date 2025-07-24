from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('edit/<int:pk>/', views.edit_transaction, name='edit_transaction'),
    path('delete/<int:pk>/', views.delete_transaction, name='delete_transaction'),
]