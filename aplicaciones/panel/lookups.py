# yourapp/lookups.py
from ajax_select import register, LookupChannel
from aplicaciones.panel.models import MediaFiles

@register('mediaimg')
class MediaTaslooup(LookupChannel):

    model = MediaFiles


    def get_query(self, q, request):
        return self.model.objects.filter(short_name__icontains=q).order_by('short_name')[:50]

    def format_item_display(self, item):
        retorno = """
        <img src="/media/{}" alt="{}" class="img-thumbnail">
        """.format(item.media_img, item.short_name)
        return retorno
        