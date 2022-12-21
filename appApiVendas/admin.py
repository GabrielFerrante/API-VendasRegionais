from django.contrib import admin
from .models import Diretor, Vendedor, Unidade, Gerente, Venda, Diretoria



@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ['data', 'hora', 'vendedor', 'valorTotal', 'latLong', 'unidadeProx', 'roaming']


@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ['user', 'unidade']

@admin.register(Diretor)
class DiretorAdmin(admin.ModelAdmin):
    list_display = ['user', 'geral']

@admin.register(Gerente)
class GerenteAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ['id', 'cidade', 'diretoria', 'latLong','gerente']

@admin.register(Diretoria)
class DiretoriaAdmin(admin.ModelAdmin):
    list_display = ['nomeDiretoria', 'diretor']