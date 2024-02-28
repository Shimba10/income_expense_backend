from django.urls import path
from .views import income_list_create_api, income_retrieve_update_destroy_api

urlpatterns = [
    path('', income_list_create_api, name='income-list-create'),
    path('<int:pk>/', income_retrieve_update_destroy_api, name='income-detail'),
]

