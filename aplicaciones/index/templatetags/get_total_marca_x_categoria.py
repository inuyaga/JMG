from django import template
from aplicaciones.panel.models import Producto
register = template.Library()

@register.filter
def get_marca_x_cat(id_categoria, marca):
    total_pro=Producto.objects.filter(prod_categoria=id_categoria, prod_marca=marca).count()
    return total_pro