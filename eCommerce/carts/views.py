from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.base import View
from goods.models import Product
from .models import Cart

class CartAdd(View):
    def get(self, request, product_slug, *args, **kwargs):
        product = Product.objects.get(slug=product_slug)
        if request.user.is_authenticated:
            carts = Cart.objects.filter(user=request.user, product=product)
            if carts.exists():
                cart = carts.first()
                if cart:
                    cart.quantity += 1
                    cart.save()
            else:
                Cart.objects.create(user=request.user, product=product, quantity=1)

        return redirect(request.META['HTTP_REFERER'])


class CartChange(DetailView):
    pass

class CartRemove(DetailView):
    pass

