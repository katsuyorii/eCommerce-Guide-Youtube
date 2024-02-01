from django.views.generic.base import TemplateView
from goods.models import Category

class Index(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['categoryes'] = Category.objects.all()

        return context


class AboutUs(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About us'
        context['categoryes'] = Category.objects.all()

        return context
