from django.urls import path
from .views import Login, Registration, Profile, logout_user

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('registration/', Registration.as_view(), name='registration'),
    path('profile/', Profile.as_view(), name='profile'),
    path('logout/', logout_user, name='logout'),
]
