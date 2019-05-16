from django.db import models

# Create your models here.
class MediaFiles(models.Model):
    media_img=models.ImageField(upload_to='MediaFiles/')
    short_name=models.CharField('Nombre', max_length=80)
    def __str__(self):
        return self.short_name

class Categoria(models.Model):
    cat=models.AutoField(primary_key=True)
    cat_nombre=models.CharField('Nombre', max_length=80, unique=True)
    def __str__(self):
        return self.cat_nombre

class Producto(models.Model):
    prod=models.AutoField(primary_key=True)
    prod_nombre=models.CharField('Nombre', max_length=80)
    prod_descripcion=models.CharField('Descripción', max_length=150)
    prod_fotos=models.ManyToManyField(MediaFiles, verbose_name='Imagenes relacionadas')
    prod_precio=models.FloatField('Precio')
    prod_descuento=models.IntegerField('Descuento sin %')
    prod_stock=models.FloatField('Cantidad de entrada a stock')
    prod_categoria=models.ForeignKey(Categoria, verbose_name='Tipo de categoria', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.prod_nombre
    

