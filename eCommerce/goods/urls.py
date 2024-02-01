from django.urls import path
from .views import Catalog

urlpatterns = [
    path('', Catalog.as_view(), name='catalog'),
]
