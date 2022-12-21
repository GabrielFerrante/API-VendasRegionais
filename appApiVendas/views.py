from datetime import date, datetime
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from .models import (
    Diretor,
    Gerente,
    Diretoria,
    Unidade,
    Venda,
    Vendedor
)
from .filters import (
    DiretorFilters,
    GerenteFilters,
    DiretoriaFilters,
    UnidadeFilters,
    VendaFilters,
    VendedorFilters
)

from .serializers import (
    DiretorSerializer,
    GerenteSerializer,
    DiretoriaSerializer,
    UnidadeSerializer,
    VendaSerializer,
    VendedorSerializer
)

#View VENDAS com GET
class VendasViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = VendaFilters

    

#View VENDA com GET, POST e PUT
class VendaViewSet(VendasViewSet, generics.RetrieveUpdateAPIView):
    
    def create(self, request):
        dados = self.get_data_venda(request=request)
        if dados != {}:
            novaVenda = Venda.objects.create(**dados)
            novaVenda.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(data="Erro ao cadastrar/algum dado incorreto",status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        venda = Venda.objects.get(id=pk)
        if venda:
            dados = self.get_data_venda(request=request)
            if  dados != {}:
                venda.data = dados['data']
                venda.hora = dados['hora']
                venda.valorTotal = dados['valorTotal']
                venda.vendedor = dados['vendedor']
                venda.unidadeProx = dados['unidadeProx']
                venda.roaming = dados['roaming']
                venda.latLong = dados['latLong']
                venda.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(data="Vendedor/Unidade inexistentes!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(data="Venda inexistente!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def validation_data_relations(self, IDvendedor, IDunidadeProx):
        vendedores = Vendedor.objects.filter(pk = IDvendedor)
        unidades = Unidade.objects.filter(pk = IDunidadeProx)
        if vendedores.count() > 0:
            if unidades.count() > 0:
                return (
                    vendedores[0],
                    unidades[0]
                )
            else:
                return 0
        else:
            return 0
    
    def get_data_venda(self,request):
        tupla = self.validation_data_relations(
            request.data['vendedor'],
            request.data['unidadeProx']
        )
        if tupla != 0:
            dados = {
                "data": request.data['data'],
                "hora": request.data['hora'],
                "valorTotal": request.data['valorTotal'],
                "latLong": request.data['latLong'],
                "roaming": request.data['roaming'],
                "unidadeProx": tupla[1],
                "vendedor": tupla[0]
            }
            return dados
        else:
            return {}

#View UNIDADE com GET
class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UnidadeFilters

#View DIRETORIA com GET
class DiretoriaViewSet(viewsets.ModelViewSet):
    queryset = Diretoria.objects.all()
    serializer_class = DiretoriaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DiretoriaFilters

#View GERENTE com GET
class GerentesViewSet(viewsets.ModelViewSet):
    queryset = Gerente.objects.all()
    serializer_class = GerenteSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GerenteFilters

#View DIRETOR com GET
class DiretorViewSet(viewsets.ModelViewSet):
    queryset = Diretor.objects.all()
    serializer_class = DiretorSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DiretorFilters

#View VENDEDOR com GET
class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = VendedorFilters