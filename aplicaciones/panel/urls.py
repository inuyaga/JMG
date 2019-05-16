from django.urls import path, include
from aplicaciones.panel import views as panel
app_name='panel'
urlpatterns = [
    path('', panel.InitPanel.as_view(), name='inicio'),
    path('tienda/producto/', panel.ProductoCrear.as_view(), name='producto_tienda'),
    path('tienda/producto/editar/<int:pk>/', panel.ProductoUpdate.as_view(), name='producto_tienda_update'),
    path('tienda/media/', panel.MediaCreate.as_view(), name='media_files'),
    path('tienda/media/get_list', panel.GetListMedia.as_view(), name='get_media_files'),
    path('tienda/media/delete/', panel.MediaDelete.as_view(), name='get_media_delete'),
    path('tienda/categoria/crear/', panel.CategoriaCrear.as_view(), name='cat_crear'),
    
]