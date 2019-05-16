from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class IndexPage(TemplateView):
    template_name='index/base.html'

class JmgShop(TemplateView):
    template_name = "index/jmg_shop.html" 

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['nav_dark'] = True
        return context
    
