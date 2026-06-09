from rest_framework import serializers
from .models import Medico, Paciente, Consulta


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'nome', 'crm', 'especialidade', 'email', 'telefone', 'ativo', 'criado_em']


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'nome', 'cpf', 'data_nascimento', 'email', 'telefone', 'convenio', 'criado_em', 'atualizado_em']


class ConsultaSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.CharField(source='paciente.nome', read_only=True)
    medico_nome = serializers.CharField(source='medico.nome', read_only=True)

    class Meta:
        model = Consulta
        fields = ['id', 'paciente', 'paciente_nome', 'medico', 'medico_nome', 'data_hora', 'status', 'observacoes', 'criado_em']
