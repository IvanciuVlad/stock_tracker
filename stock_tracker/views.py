from django.views.generic import TemplateView


class HelloPage(TemplateView):
    template_name = "hello.html"


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class HomePage(TemplateView):
    template_name = 'index.html'
