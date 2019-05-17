from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, View, UpdateView, DeleteView, View
from aplicaciones.panel.models import Producto, Categoria, MediaFiles
from aplicaciones.panel.forms import ProductoForm, MediaForm, CategoriaForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from aplicaciones.index.eliminaciones import get_deleted_objects
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# Create your views here.
class InitPanel(TemplateView):
    template_name='panel/inicio.html'



class ProductoCrear(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'next'
    model = Producto
    template_name = "panel/crear.html"
    form_class = ProductoForm
    success_url = reverse_lazy('panel:producto_tienda')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_prod'] = Producto.objects.all()

        
        return context

class ProductoDelete(DeleteView):
    model = Producto
    template_name='eliminaciones.html'
    success_url = reverse_lazy('panel:producto_tienda')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        deletable_objects, model_count, protected = get_deleted_objects([self.object])
        #
        context['deletable_objects']=deletable_objects
        context['model_count']=dict(model_count).items()
        context['protected']=protected
        
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

class CategoriaCrear(TemplateView):
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
    
class CategiriaCreateView(CreateView):
    model = Categoria
    template_name='panel/create_generico.html'
    form_class=CategoriaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_data'] = Categoria.objects.all()
        
        return context


class CategoriaDelete(DeleteView):
    model = Categoria
    template_name='eliminaciones.html'
    success_url = reverse_lazy('panel:cat_create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        deletable_objects, model_count, protected = get_deleted_objects([self.object])
        #
        context['deletable_objects']=deletable_objects
        context['model_count']=dict(model_count).items()
        context['protected']=protected
        
        return context

class CategoriaUpdate(View):
    def post(self, request, *args, **kwargs):
        from django.db import IntegrityError
        import json
        # body_unicode = request.body.decode('utf-8')
        body = json.loads(request.body)
        try:
            ID=body.get('ID')
            text_update=body.get('valor')
            Categoria.objects.filter(cat=ID).update(cat_nombre=text_update)
            catergoria=Categoria.objects.filter(cat=ID).values()
            cat_list=list(catergoria)
            data = {
                    'cat_list': cat_list,
                    'status': True,
                }
            return JsonResponse(data) 
        except IntegrityError as e:
            # Do something based on the errors contained in e.message_dict.
            # Display them to a user, or handle them programmatically.            
            data = {
                    'error': 'error',
                    'type': 'Ya existe un elemento con ese nombre',
                    'status': False,
                }
            return JsonResponse(data, status=400)
        
    



