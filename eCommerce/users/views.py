from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm

class Login(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'

        return context

class Registration(TemplateView):
    template_name = 'users/registration.html'

class Profile(TemplateView):
    template_name = 'users/profile.html'