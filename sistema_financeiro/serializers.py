from rest_framework import serializers
from .models import Categoria, Despesa, Receita


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'tipo', 'criado_em']


class DespesaSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)

    class Meta:
        model = Despesa
        fields = ['id', 'descricao', 'valor', 'data', 'categoria', 'categoria_nome', 'pago', 'criado_em', 'atualizado_em']


class ReceitaSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)

    class Meta:
        model = Receita
        fields = ['id', 'descricao', 'valor', 'data', 'categoria', 'categoria_nome', 'recebido', 'criado_em', 'atualizado_em']
