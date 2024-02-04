from django.urls import path
from .views import Login, Registration, Profile, logout_user
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('registration/', Registration.as_view(), name='registration'),
    path('profile/', login_required(Profile.as_view()), name='profile'),
    path('logout/', login_required(logout_user), name='logout'),
]
