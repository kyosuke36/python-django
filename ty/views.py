from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'ty/index.html'