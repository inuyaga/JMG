# Generated by Django 2.2.1 on 2019-05-14 20:08

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
                ('cat_nombre', models.CharField(max_length=80, verbose_name='Nombre')),
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
                ('prod_nombre', models.CharField(max_length=80, verbose_name='Nombre')),
                ('prod_descripcion', models.CharField(max_length=150, verbose_name='Descripción')),
                ('prod_precio', models.FloatField(verbose_name='Precio')),
                ('prod_descuento', models.IntegerField(verbose_name='Descuento sin %')),
                ('prod_stock', models.FloatField(verbose_name='Cantidad de entrada a stock')),
                ('prod_categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='panel.Categoria', verbose_name='Tipo de categoria')),
                ('prod_fotos', models.ManyToManyField(to='panel.MediaFiles', verbose_name='Imagenes relacionadas')),
            ],
        ),
    ]
