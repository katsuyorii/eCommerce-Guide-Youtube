from django.views.generic.base import TemplateView


class Catalog(TemplateView):
    template_name = 'goods/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Catalog'

        return context
