from django.db import models
import random
# Create your models here.
class MediaFiles(models.Model):
    media_img=models.ImageField(upload_to='MediaFiles/')
    short_name=models.CharField('Nombre', max_length=80)
    def __str__(self):
        return self.short_name

class Categoria(models.Model):
    cat=models.AutoField(primary_key=True)
    cat_nombre=models.CharField('Categoria', max_length=80, unique=True)
    def __str__(self):
        return self.cat_nombre

class Marcas(models.Model):
    marca=models.AutoField(primary_key=True)
    marca_nombre=models.CharField('Marca', max_length=80, unique=True) 
    def total_prod_marca(self):
        total=Producto.objects.filter(prod_marca=self.marca).count()
        return total
    def __str__(self):
        return self.marca_nombre 

class Producto(models.Model): 
    prod=models.AutoField(primary_key=True)
    prod_codigo=models.CharField('Codigo producto', max_length=35, unique=True)
    prod_nombre=models.CharField('Nombre', max_length=80)
    prod_descripcion=models.TextField('Descripción')
    prod_miniatura=models.ImageField('Miniatura', upload_to='MediaFiles/miniaturas')
    prod_fotos=models.ManyToManyField(MediaFiles, verbose_name='Imagenes relacionadas')
    prod_precio=models.FloatField('Precio')
    prod_descuento=models.IntegerField('Descuento sin %')
    prod_stock=models.FloatField('Cantidad de entrada a stock')
    prod_categoria=models.ForeignKey(Categoria, verbose_name='Tipo de categoria', on_delete=models.SET_NULL, blank=True, null=True)
    prod_marca=models.ForeignKey(Marcas, verbose_name='Marca', on_delete=models.CASCADE)
    prod_fecha_creacion=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.prod_codigo
    def prod_con_descuento(self): 
        precio=self.prod_precio
        descuento=self.prod_descuento
        resultado_descuento=descuento/100
        descuentoR=precio*resultado_descuento
        return round(precio-descuentoR, 2)


class ItemEspecificacion(models.Model):
    item=models.AutoField(primary_key=True)
    item_nombre=models.CharField('Item', max_length=80, unique=True)
    def __str__(self):
        return self.item_nombre

class EspecificacionProducto(models.Model):
    esp=models.AutoField(primary_key=True)
    esp_item=models.ForeignKey(ItemEspecificacion, verbose_name='Item', on_delete=models.CASCADE)
    esp_especificacion=models.CharField('Especificacion', max_length=50)
    esp_producto=models.ForeignKey(Producto, verbose_name='Producto', on_delete=models.CASCADE)
    def __str__(self):
        item=str(self.esp_item)
        esp=str(self.esp_especificacion)
        return item + ' ' +esp
    class Meta:
        unique_together = (("esp_item", "esp_producto"),)
        

    

