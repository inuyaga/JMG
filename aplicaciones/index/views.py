from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from aplicaciones.panel.models import Producto, Categoria, EspecificacionProducto
from django.db.models import Q, F, Sum, FloatField
from django.contrib.postgres.search import SearchVector
from aplicaciones.panel.models import Marcas, Producto
from django.urls import reverse_lazy
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

class add_compra(TemplateView): 
    template_name = "index/detalle_producto.html"
    def get(self, request, *args, **kwargs):
        codigo=kwargs.get('codigo')
        cantidad=kwargs.get('cantidad')
        detail=request.GET.get('detalle')
        url=''
        if 'compra' not in request.session:
            request.session['compra']={codigo:cantidad}
            request.session['compra_items']=len(request.session['compra'])
        else:
            request.session['compra'].update({codigo:cantidad})
            request.session['compra_items']=len(request.session['compra'])
        
        
        url=reverse_lazy('index:detalle', kwargs={'pk':detail})
        return redirect(url)

class CheckListCompra(TemplateView):
    template_name = "index/check_list.html"
    def get_context_data(self, **kwargs):
        from django.contrib.humanize.templatetags.humanize import intcomma as intcomma_django
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context['detalles_obj'] = EspecificacionProducto.objects.filter(esp_producto=self.kwargs.get('pk'))
        tab=""
        
        try:
            codigos_prod=self.request.session.get('compra').keys()
            codigos_prod_all=self.request.session.get('compra')
            productos_list=Producto.objects.filter(prod_codigo__in=codigos_prod).annotate(descuento=Sum(F('prod_precio') * F('prod_descuento')/100, output_field=FloatField()))
            print(productos_list)
            total=0
            for item in productos_list:
                subtotal = round(codigos_prod_all[item.prod_codigo] * item.prod_precio-(codigos_prod_all[item.prod_codigo]*item.descuento), 3)
                total += subtotal
                tem = """
                <tr>
                    <td>
                        <div class="media">
                            <div class="d-flex">
                                <img src="{imagen}" alt="" width="80px" height="80px">
                            </div>
                            <div class="media-body">
                                <p>{nombre}</p>
                            </div>
                        </div>
                    </td>
                    <td>
                        <h5>${precio}</h5>
                    </td>
                    <td>
                    
                    <div class="form-group col-md-4">
                                <input type="number" value="{cantidad}" min="1" class="form-control" name="" id="">
                        </div>
                        
                    </td>
                    <td>
                        <h5>${total}</h5>
                    </td>
                </tr>
                """.format(imagen=str(item.prod_miniatura.url),nombre=item.prod_nombre,precio=intcomma_django( round(item.prod_precio-item.descuento, 3)),cantidad=str(codigos_prod_all[item.prod_codigo]),total=intcomma_django(subtotal))
                
                
                tab += tem
            context['tabla']=tab           
            context['total']=intcomma_django(total)
        except Exception as err:
            print(err)
                   
            
        return context

        
