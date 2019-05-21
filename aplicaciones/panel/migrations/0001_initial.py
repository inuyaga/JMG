# Generated by Django 2.2.1 on 2019-05-21 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('cat', models.AutoField(primary_key=True, serialize=False)),
                ('cat_nombre', models.CharField(max_length=80, unique=True, verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='ItemEspecificacion',
            fields=[
                ('item', models.AutoField(primary_key=True, serialize=False)),
                ('item_nombre', models.CharField(max_length=80, unique=True, verbose_name='Item')),
            ],
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('marca', models.AutoField(primary_key=True, serialize=False)),
                ('marca_nombre', models.CharField(max_length=80, unique=True, verbose_name='Marca')),
            ],
        ),
        migrations.CreateModel(
            name='MediaFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_img', models.ImageField(upload_to='MediaFiles/')),
                ('short_name', models.CharField(max_length=80, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('prod', models.AutoField(primary_key=True, serialize=False)),
                ('prod_codigo', models.CharField(max_length=35, unique=True, verbose_name='Codigo producto')),
                ('prod_nombre', models.CharField(max_length=80, verbose_name='Nombre')),
                ('prod_descripcion', models.TextField(verbose_name='Descripción')),
                ('prod_miniatura', models.ImageField(upload_to='MediaFiles/miniaturas', verbose_name='Miniatura')),
                ('prod_precio', models.FloatField(verbose_name='Precio')),
                ('prod_descuento', models.IntegerField(verbose_name='Descuento sin %')),
                ('prod_stock', models.FloatField(verbose_name='Cantidad de entrada a stock')),
                ('prod_categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='panel.Categoria', verbose_name='Tipo de categoria')),
                ('prod_fotos', models.ManyToManyField(to='panel.MediaFiles', verbose_name='Imagenes relacionadas')),
                ('prod_marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.Marcas', verbose_name='Marca')),
            ],
        ),
        migrations.CreateModel(
            name='EspecificacionProducto',
            fields=[
                ('esp', models.AutoField(primary_key=True, serialize=False)),
                ('esp_especificacion', models.CharField(max_length=50, verbose_name='Especificacion')),
                ('esp_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.ItemEspecificacion', verbose_name='Item')),
                ('esp_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.Producto', verbose_name='Producto')),
            ],
        ),
    ]
