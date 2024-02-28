from django.urls import path
from .views import expense_list_create_api, expense_retrieve_update_destroy_api

urlpatterns = [
    path('', expense_list_create_api, name='expense-list-create'),
    path('<int:pk>/', expense_retrieve_update_destroy_api, name='expense-detail'),
]