from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "event/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "３０秒でつくれる！カンタン出欠表"
        return context
