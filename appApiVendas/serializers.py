from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Diretor, 
    Gerente, 
    Diretoria, 
    Unidade,
    Venda, 
    Vendedor
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name','email']

class GerenteSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Gerente
        fields = ['id','user']
    
class DiretorSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Diretor
        fields = ['id','user', 'geral']

class DiretoriaSerializer(serializers.ModelSerializer):
    diretor = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = Diretoria
        fields = ['id','nomeDiretoria', 'diretor']

class UnidadeSerializer(serializers.ModelSerializer):
    diretoria = DiretoriaSerializer(many=False, read_only=True)
    gerente = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = Unidade
        fields = ['id', 'cidade', 'diretoria', 'latLong','gerente']

class VendedorSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    unidade = UnidadeSerializer(many=False, read_only=True)
    class Meta:
        model = Vendedor
        fields = ['id','user', 'unidade']



class VendaSerializer(serializers.ModelSerializer):
    vendedor = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    unidadeProx = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Venda
        fields = ['id','data', 'hora', 'vendedor', 'valorTotal', 'latLong', 'unidadeProx', 'roaming']

    


