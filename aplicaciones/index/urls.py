from django.urls import path, include
from aplicaciones.index import views as index
app_name='index'
urlpatterns = [
    path('', index.IndexPage.as_view(), name='inicio'),
    path('jmg-shoping/', index.JmgShop.as_view(), name='shop'),
]