from django.views.generic.base import TemplateView

class Login(TemplateView):
    template_name = 'users/login.html'

class Registration(TemplateView):
    template_name = 'users/registration.html'

class Profile(TemplateView):
    template_name = 'users/profile.html'