from django import forms
from aplicaciones.panel.models import Producto, MediaFiles, Categoria, EspecificacionProducto
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
class EspeficicacionForm(forms.ModelForm): 
    class Meta:
        model = EspecificacionProducto
        fields = ('esp_item','esp_especificacion')
    def __init__(self, *args, **kwargs):
        super(EspeficicacionForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})