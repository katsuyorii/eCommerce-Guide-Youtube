from django.views.generic.base import TemplateView
from .models import Category

class Catalog(TemplateView):
    template_name = 'goods/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Catalog'
        context['categoryes'] = Category.objects.all()

        return context
