from django.contrib import admin

from apps.galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id","nome","legenda","publicada")#mostra as referencias de título dos campos
    list_display_links = ("id", "nome") #campos que eu quero que sejam links que levam para aquele campo
    search_fields = ("nome",) #campo de busca, e precisa da vírugula no final pois é uma tuple
    list_filter = ("categoria","usuario",) #permite filtrar por categoria
    list_editable = ("publicada",) #permite selecionar se quer publicar ou nao
    list_per_page = 10 #mostra 10 itens por página

admin.site.register(Fotografia, ListandoFotografias) #aqui que ele faz o registro do que determinando como configurações