from rest_framework import viewsets
from .models import Especialidade, Medico, Paciente, AgendamentoConsulta
from .serializers import EspecialidadeSerializer, MedicoSerializer, PacienteSerializer, AgendamentoConsultaSerializer


class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class AgendamentoConsultaViewSet(viewsets.ModelViewSet):
    queryset = AgendamentoConsulta.objects.all()
    serializer_class = AgendamentoConsultaSerializer
