from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import (
    LoginView,
    SignUpView,
)

app_name = "users"

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('signup', SignUpView.as_view(), name='sign-up'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
