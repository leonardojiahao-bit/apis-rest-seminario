from rest_framework import serializers
from .models import Especialidade, Medico, Paciente, AgendamentoConsulta


class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ['id', 'nome', 'descricao']


class MedicoSerializer(serializers.ModelSerializer):
    especialidade_nome = serializers.CharField(source='especialidade.nome', read_only=True)

    class Meta:
        model = Medico
        fields = ['id', 'nome', 'crm', 'especialidade', 'especialidade_nome', 'ativo', 'criado_em']


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'nome', 'cpf', 'sus', 'data_nascimento', 'telefone', 'email', 'criado_em', 'atualizado_em']


class AgendamentoConsultaSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.CharField(source='paciente.nome', read_only=True)
    medico_nome = serializers.CharField(source='medico.nome', read_only=True)
    especialidade_nome = serializers.CharField(source='medico.especialidade.nome', read_only=True)

    class Meta:
        model = AgendamentoConsulta
        fields = ['id', 'paciente', 'paciente_nome', 'medico', 'medico_nome', 'especialidade_nome', 'data_hora', 'status', 'motivo', 'observacoes', 'criado_em', 'atualizado_em']
