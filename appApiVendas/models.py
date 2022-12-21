
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User, Group

# Create your models here.


class Diretor(models.Model):
    user = models.OneToOneField(
        User, related_name='diretor', on_delete=models.CASCADE)
    geral = models.BooleanField("Diretor geral", default=None)

    class Meta:
        verbose_name = 'Diretor'
        verbose_name_plural = 'Diretores'
    
    def __str__(self):
        return self.user.first_name + " "+ self.user.last_name


class Gerente(models.Model):
    user = models.OneToOneField(
        User, related_name='gerente', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Gerente'
        verbose_name_plural = 'Gerentes'

    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Diretoria(models.Model):
    nomeDiretoria = models.CharField("Região", max_length=100)
    diretor = models.OneToOneField(Diretor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Diretoria'
        verbose_name_plural = 'Diretorias'

    def __str__(self):
        return self.nomeDiretoria

class Unidade(models.Model):
    latLong = models.CharField("Latitude e Longitude", max_length=130, default=None)
    cidade = models.CharField("Cidade", max_length=100, default=None)
    diretoria = models.ForeignKey(Diretoria, on_delete=models.CASCADE)
    gerente = models.OneToOneField(Gerente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'

    def __str__(self):
        return self.cidade

class Vendedor(models.Model):
    user = models.OneToOneField(
        User, related_name='vendedor', on_delete=models.CASCADE)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class Venda(models.Model):
    data = models.DateField("Data")
    hora = models.TimeField("Hora")
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    valorTotal = models.FloatField("Valor total", default=None)
    latLong = models.CharField("Latitude e Longitude", max_length=130, default=None)
    unidadeProx = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    roaming = models.BooleanField("Roaming?")

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
