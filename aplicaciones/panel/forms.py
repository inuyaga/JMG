from django import forms
from aplicaciones.panel.models import Producto, MediaFiles, Categoria
from ajax_select.fields import AutoCompleteSelectMultipleField


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
    prod_fotos = AutoCompleteSelectMultipleField('mediaimg',required=False, help_text='Escriba nombre de la imagen a buscar')
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        self.fields['prod_nombre'].widget.attrs.update({'v-model': 'prod_nombre'})
        self.fields['prod_descripcion'].widget.attrs.update({'v-model': 'prod_descripcion'})
        self.fields['prod_fotos'].widget.attrs.update({'v-model': 'prod_fotos'})
        self.fields['prod_precio'].widget.attrs.update({'v-model': 'prod_precio'})
        self.fields['prod_descuento'].widget.attrs.update({'v-model': 'prod_descuento'})
        self.fields['prod_stock'].widget.attrs.update({'v-model': 'prod_stock'})
        self.fields['prod_categoria'].widget.attrs.update({'v-model': 'prod_categoria'})

class MediaForm(forms.ModelForm):
    class Meta:
        model = MediaFiles
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(MediaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        self.fields['media_img'].widget.attrs.update({'@change': 'processFile($event)'})
        self.fields['short_name'].widget.attrs.update({'v-model': 'short_name'})

class CategoriaForm(forms.ModelForm): 
    class Meta:
        model = Categoria
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})