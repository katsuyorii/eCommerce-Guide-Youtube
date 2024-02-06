from django.urls import path
from .views import CartAdd, CartChange, CartRemove

urlpatterns = [
    path('cart_add/<slug:product_slug>', CartAdd.as_view(), name='cart_add'),\
    path('cart_change/<slug:product_slug>', CartChange.as_view(), name='cart_change'),
    path('cart_remove/<slug:product_slug>', CartRemove.as_view(), name='cart_remove'),
]