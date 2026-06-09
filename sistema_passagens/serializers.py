from rest_framework import serializers
from .models import Aeroporto, Voo, Passagem


class AeroportoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeroporto
        fields = ['id', 'nome', 'codigo_iata', 'cidade', 'pais']


class VooSerializer(serializers.ModelSerializer):
    origem_cidade = serializers.CharField(source='origem.cidade', read_only=True)
    destino_cidade = serializers.CharField(source='destino.cidade', read_only=True)

    class Meta:
        model = Voo
        fields = ['id', 'numero_voo', 'origem', 'origem_cidade', 'destino', 'destino_cidade', 'data_partida', 'data_chegada', 'capacidade', 'preco_base', 'status', 'criado_em']


class PassagemSerializer(serializers.ModelSerializer):
    voo_numero = serializers.CharField(source='voo.numero_voo', read_only=True)

    class Meta:
        model = Passagem
        fields = ['id', 'voo', 'voo_numero', 'passageiro_nome', 'passageiro_cpf', 'assento', 'classe', 'preco', 'status', 'criado_em', 'atualizado_em']
