from django.urls import path
from .views import Catalog, ProductDetail

urlpatterns = [
    path('', Catalog.as_view(), name='catalog'),
    path('product/<slug:product_slug>/', ProductDetail.as_view(), name='product_detail'),
]
