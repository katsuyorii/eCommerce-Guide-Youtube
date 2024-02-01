from django.urls import path
from .views import Index, AboutUs

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', AboutUs.as_view(), name='about'),
]
