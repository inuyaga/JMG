from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from aplicaciones.panel.models import Producto, Categoria, EspecificacionProducto
from django.db.models import Q
from django.contrib.postgres.search import SearchVector
from aplicaciones.panel.models import Marcas, Producto
# Create your views here.
class IndexPage(TemplateView):
    template_name='index/base.html'

class JmgShop(TemplateView): 
    template_name = "index/base_tienda.html"  

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['nav_dark'] = True
        context['categira_list'] = Categoria.objects.all()
        categoria=self.request.GET.get('cat')
        buscar=self.request.GET.get('buscar')
        query = Producto.objects.all()
        context['busqueda'] = buscar
        context['last_prod_list'] = Producto.objects.all().order_by('-prod_fecha_creacion')[:8]
        if categoria != '':
            context['object_list'] = query.filter(prod_categoria=categoria)

        if buscar != None:
            context['object_list'] = query.annotate(search=SearchVector('prod_nombre', 'prod_descripcion')).filter(search=buscar)
            
        return context

class JmgShopBuscar(ListView):
    model=Producto
    template_name = "index/jmg_shop.html"  
    paginate_by = 50
    
    def get_queryset(self, *args, **kwargs):
        queryset = super(JmgShopBuscar, self).get_queryset()
        categoria=self.request.GET.get('cat')
        buscar=self.request.GET.get('buscar')
        marca=self.request.GET.get('marca')
        query = Producto.objects.all()
        if categoria != None:
            queryset = queryset.filter(prod_categoria=categoria)
            if marca != None:
                queryset = queryset.filter(prod_marca=marca)
        if buscar != None:
            queryset = queryset.annotate(search=SearchVector('prod_nombre', 'prod_descripcion')).filter(search=buscar)

        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['nav_dark'] = True
        context['categira_list'] = Categoria.objects.all()
        context['marcas_list'] = Marcas.objects.all()
        context['busqueda'] = self.request.GET.get('buscar')
        context['categoria'] = self.request.GET.get('cat')
        context['marca'] = self.request.GET.get('marca')
            
        return context
class TiendaDetalleProducto(DetailView):
    model=Producto
    template_name = "index/detalle_producto.html"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['detalles_obj'] = EspecificacionProducto.objects.filter(esp_producto=self.kwargs.get('pk'))
        context['categira_list'] = Categoria.objects.all()
            
        return context
    
