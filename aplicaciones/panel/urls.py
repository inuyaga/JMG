from django.urls import path, include
from aplicaciones.panel import views as panel
app_name='panel'
urlpatterns = [
    path('', panel.InitPanel.as_view(), name='inicio'),
    path('tienda/producto/', panel.ProductoCrear.as_view(), name='producto_tienda'),
    path('tienda/producto/editar/<int:pk>/', panel.ProductoUpdate.as_view(), name='producto_tienda_update'),
    path('tienda/producto/delete/<int:pk>/', panel.ProductoDelete.as_view(), name='producto_tienda_delete'),
    path('tienda/media/', panel.MediaCreate.as_view(), name='media_files'),
    path('tienda/media/get_list', panel.GetListMedia.as_view(), name='get_media_files'),
    path('tienda/media/delete/', panel.MediaDelete.as_view(), name='get_media_delete'),

    path('tienda/categoria/crear/', panel.CategoriaCrear.as_view(), name='cat_crear'),
    path('tienda/categoria/create/', panel.CategiriaCreateView.as_view(), name='cat_create'),
    path('tienda/categoria/delete/<int:pk>/', panel.CategoriaDelete.as_view(), name='cat_delete'),
    path('tienda/categoria/update/', panel.CategoriaUpdate.as_view(), name='cat_update'),

    path('tienda/marca/crear/', panel.MarcaCrear.as_view(), name='marca_crar'),

    path('tienda/item/crear/', panel.ItemCrear.as_view(), name='item_crar'),

    path('tienda/producto/especificaciones/<int:pk>/', panel.EspecificacionCrear.as_view(), name='especificacion'),
    
] 