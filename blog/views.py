from django.shortcuts import render
from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(f"Trying to load template: {self.template_name}")
        return context


class ContactPage(TemplateView):
    template_name = 'blog/contact.html'
