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

#View de vendas
#Retorna todas as vendas
class VendasViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = VendaFilters

    def create(self, request):
        vendedor = Vendedor.objects.filter(pk = request.data['vendedor'])[0]
        unidadeProx = Unidade.objects.filter(pk = request.data['unidadeProx'])[0]
        novaVenda = Venda.objects.create(
            data= request.data['data'],
            hora= request.data['hora'],
            valorTotal =request.data['valorTotal'],
            vendedor = vendedor,
            unidadeProx = unidadeProx,
            roaming = request.data['roaming'],
            latLong = request.data['latLong']
        )
        novaVenda.save()
        return Response(status=status.HTTP_201_CREATED)
        
#View com GET E POST
class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UnidadeFilters

#View com GET E POST
class DiretoriaViewSet(viewsets.ModelViewSet):
    queryset = Diretoria.objects.all()
    serializer_class = DiretoriaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DiretoriaFilters

#View com GET E POST
class GerentesViewSet(viewsets.ModelViewSet):
    queryset = Gerente.objects.all()
    serializer_class = GerenteSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GerenteFilters

#View com GET E POST
class DiretorViewSet(viewsets.ModelViewSet):
    queryset = Diretor.objects.all()
    serializer_class = DiretorSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DiretorFilters

#View com GET E POST
class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = VendedorFilters