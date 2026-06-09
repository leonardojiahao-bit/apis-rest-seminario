from rest_framework import serializers
from .models import Aluno, Plano, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'cpf', 'email', 'telefone', 'data_nascimento', 'ativo', 'criado_em', 'atualizado_em']


class PlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plano
        fields = ['id', 'nome', 'descricao', 'valor_mensal', 'duracao_meses', 'ativo']


class MatriculaSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.CharField(source='aluno.nome', read_only=True)
    plano_nome = serializers.CharField(source='plano.nome', read_only=True)

    class Meta:
        model = Matricula
        fields = ['id', 'aluno', 'aluno_nome', 'plano', 'plano_nome', 'data_inicio', 'data_fim', 'ativa', 'criado_em']
