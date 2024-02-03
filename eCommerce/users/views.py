from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from .forms import UserLoginForm, UserRegistrationForm

class Login(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'

        return context

class Registration(CreateView):
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'

    def get_success_url(self):
        return reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registration'

        return context

class Profile(TemplateView):
    template_name = 'users/profile.html'