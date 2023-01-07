from django.urls import path
from .views import LoginPage, SignUpView

urlpatterns = [
    path("login/", LoginPage.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
