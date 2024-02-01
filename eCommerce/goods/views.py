from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Product

class Catalog(ListView):
    model = Product
    template_name = 'goods/catalog.html'
    context_object_name = 'products'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Catalog'
        context['categoryes'] = Category.objects.all()

        return context
    

class ProductDetail(DetailView):
    model = Product
    template_name = 'goods/product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Product'
        context['categoryes'] = Category.objects.all()

        return context