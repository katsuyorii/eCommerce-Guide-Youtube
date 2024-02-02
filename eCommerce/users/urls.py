from django.urls import path
from .views import Login, Registration, Profile

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('registration/', Registration.as_view(), name='registration'),
    path('profile/', Profile.as_view(), name='profile'),
    path('logout/', Profile.as_view(), name='logout'),
]
