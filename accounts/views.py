from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserLoginForm, CustomSignUpForm


class LoginPage(LoginView):
    authentication_form = CustomUserLoginForm


class SignUpView(CreateView):
    form_class = CustomSignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
