from django.db.models.query import QuerySet
from django.views.generic.list import ListView
from .models import Category, Product

class Catalog(ListView):
    model = Product
    template_name = 'goods/catalog.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Catalog'
        context['categoryes'] = Category.objects.all()

        return context