from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from .models import User
from django.contrib import messages

class Login(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        messages.success(self.request, 'Вы вошли в аккаунт!')
        return super().form_valid(form)
    
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

def logout_user(request):
    logout(request)
    return redirect(reverse('index'))

class Profile(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
    '''Переопределение метода, чтобы вернуть текущего пользователя, дабы не добавлять pk или slug в url'''
    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'User profile'

        return context
    

class UsersCart(TemplateView):
    template_name = 'users/users-cart.html'

