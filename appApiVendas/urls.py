from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (
    VendasViewSet,
    VendaViewSet,
    UnidadeViewSet,
    DiretoriaViewSet,
    DiretorViewSet,
    GerentesViewSet,
    VendedorViewSet
)

router = SimpleRouter()
router.register('vendas', VendasViewSet) #/api/v1/vendas
router.register('venda', VendaViewSet) #/api/v1/venda
router.register('unidades', UnidadeViewSet) #/api/v1/unidades
router.register('diretorias', DiretoriaViewSet) #/api/v1/diretorias
router.register('diretores', DiretorViewSet) #/api/v1/diretores
router.register('gerentes', GerentesViewSet) #/api/v1/gerentes
router.register('vendedores', VendedorViewSet) #/api/v1/vendedores

