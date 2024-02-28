from django.urls import path

from user.views import login_user, register_user


urlpatterns = [
    path('register/', register_user, name='register'),
    path('', login_user, name='login'),
]