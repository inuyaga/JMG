from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, View, UpdateView
from aplicaciones.panel.models import Producto, Categoria, MediaFiles
from aplicaciones.panel.forms import ProductoForm, MediaForm, CategoriaForm
from django.urls import reverse_lazy
from django.http import JsonResponse
# Create your views here.
# Create your views here.
class InitPanel(TemplateView):
    template_name='panel/inicio.html'


class ProductoCrear(CreateView):
    model = Producto
    template_name = "panel/crear.html"
    form_class = ProductoForm
    success_url = reverse_lazy('panel:producto_tienda')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_prod'] = Producto.objects.all()
        
        return context

class ProductoUpdate(UpdateView):
    model = Producto
    template_name = "panel/producto_editar.html"
    form_class = ProductoForm
    success_url = reverse_lazy('panel:producto_tienda')



class AjaxMediaResponse:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            media=MediaFiles.objects.values('id','media_img', 'short_name')
            media_list=list(media)
            data = {
                'pk': self.object.pk,
                'imgs': media_list,
            }
            return JsonResponse(data)
        else:
            return response

class MediaCreate(AjaxMediaResponse, CreateView):
    model = MediaFiles
    template_name = "panel/crear_medias.html"
    form_class = MediaForm
    success_url = reverse_lazy('panel:producto_tienda')

class GetListMedia(View):
    def get(self, request, *args, **kwargs):
        media=MediaFiles.objects.values('id','media_img', 'short_name')
        media_list=list(media)
        data = {
                'imgs': media_list,
            }
        return JsonResponse(data)
class MediaDelete(View):
    def get(self, request, *args, **kwargs):
        from django.core.files.storage import default_storage
        # OBTENEMOS EL ID A ELIMINAR DEL MEDIA
        id_name=request.GET.get('delete_id')
        # OBTENEMOS EL ARCHIVO DE IMAGEN DE LA BD
        img=MediaFiles.objects.get(id=id_name)
        # ELIMINAMOS EL OBJETO DE LA BD
        MediaFiles.objects.filter(id=id_name).delete()
        # ELIMINAMOS EL ARCHIVO DEL STORAGE
        default_storage.delete(img.media_img.path)
        # OBTENEMOS LA NUEVA LISTA ACTUALIZADA
        media=MediaFiles.objects.values('id','media_img', 'short_name')

        media_list=list(media)
        data = {
                'imgs': media_list,
            }

        return JsonResponse(data)



class AjaxCategoriaResponse:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        # print(form)
        # print(self.object)
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        print(self)
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response

class CategoriaCrear(AjaxCategoriaResponse, TemplateView):
    model=Categoria
    template_name='panel/crear_medias.html'
    form_class = CategoriaForm
    def post(self, request, *args, **kwargs):
        from django.core.exceptions import ValidationError
        import json
        # body_unicode = request.body.decode('utf-8')
        body = json.loads(request.body)
        try:
            categoriObj=Categoria(cat_nombre=body.get('cat_nombre').title())
            categoriObj.full_clean()
            categoriObj.save()
            catergoria=Categoria.objects.filter(cat=categoriObj.pk).values()
            cat_list=list(catergoria)
            data = {
                    'cat_list': cat_list,
                    'status': True,
                }
            return JsonResponse(data) 
        except ValidationError as e:
            # Do something based on the errors contained in e.message_dict.
            # Display them to a user, or handle them programmatically.
            
            data = {
                    'error': 'error',
                    'type': dict(e),
                    'status': False,
                    
                }
            return JsonResponse(data, status=400)
    
            

        
        
        
    



