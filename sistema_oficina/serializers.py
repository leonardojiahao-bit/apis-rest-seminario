from rest_framework import serializers
from .models import Cliente, Veiculo, OrdemServico


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf_cnpj', 'telefone', 'email', 'endereco', 'criado_em', 'atualizado_em']


class VeiculoSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.CharField(source='cliente.nome', read_only=True)

    class Meta:
        model = Veiculo
        fields = ['id', 'cliente', 'cliente_nome', 'placa', 'marca', 'modelo', 'ano', 'cor', 'criado_em']


class OrdemServicoSerializer(serializers.ModelSerializer):
    veiculo_placa = serializers.CharField(source='veiculo.placa', read_only=True)
    cliente_nome = serializers.CharField(source='veiculo.cliente.nome', read_only=True)

    class Meta:
        model = OrdemServico
        fields = ['id', 'veiculo', 'veiculo_placa', 'cliente_nome', 'descricao', 'status', 'valor_total', 'data_entrada', 'data_saida', 'criado_em', 'atualizado_em']
