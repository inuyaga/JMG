from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class InitTickets(TemplateView):
    template_name='tickets/inicio.html'

