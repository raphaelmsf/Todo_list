from django.contrib import admin
from .models import Projeto

class ListandoProjetos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'status', 'publicado')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('publicado',)
    list_editable = ('publicado',)
    list_per_page = 5

admin.site.register(Projeto, ListandoProjetos)