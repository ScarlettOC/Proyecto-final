from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'home.html'

class MateaView(TemplateView):
    template_name = 'matea.html'

