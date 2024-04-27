from django.contrib import admin

from galeria.models import Fotografia


class ListandoFotografia(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 20


# Register your models here.
admin.site.register(Fotografia, ListandoFotografia)
