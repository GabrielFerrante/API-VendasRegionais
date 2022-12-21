from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from .models import (
    Diretor, 
    Gerente, 
    Diretoria, 
    Unidade,
    Venda, 
    Vendedor
)

#Definindo os filtros de endpoint para cada modelo
class VendaFilters(filters.FilterSet):

    CriadoHoraMin = filters.TimeFilter(field_name="hora", lookup_expr='gte')
    CriadoHoraMax = filters.TimeFilter(field_name="hora", lookup_expr='lte')

    CriadoDataMin = filters.DateFilter(field_name="data", lookup_expr='gte')
    CriadoDataMax = filters.DateFilter(field_name="data", lookup_expr='lte')

    class Meta:
        model = Venda
        fields = '__all__'

class UnidadeFilters(filters.FilterSet):

    class Meta:
        model = Unidade
        fields = '__all__'

class DiretoriaFilters(filters.FilterSet):

    class Meta:
        model = Diretoria
        fields = '__all__'

class DiretorFilters(filters.FilterSet):

    class Meta:
        model = Diretor
        fields = '__all__'

class GerenteFilters(filters.FilterSet):

    class Meta:
        model = Gerente
        fields = '__all__'

class VendedorFilters(filters.FilterSet):

    class Meta:
        model = Vendedor
        fields = '__all__'