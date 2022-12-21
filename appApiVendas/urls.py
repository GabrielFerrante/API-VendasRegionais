from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (
    VendasViewSet,
    UnidadeViewSet,
    DiretoriaViewSet,
    DiretorViewSet,
    GerentesViewSet,
    VendedorViewSet
)

router = SimpleRouter()
router.register('vendas', VendasViewSet)
router.register('unidades', UnidadeViewSet)
router.register('diretorias', DiretoriaViewSet)
router.register('diretores', DiretorViewSet)
router.register('gerentes', GerentesViewSet)
router.register('vendedores', VendedorViewSet)
