from rest_framework import viewsets
from .models import Aluno, Plano, Matricula
from .serializers import AlunoSerializer, PlanoSerializer, MatriculaSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class PlanoViewSet(viewsets.ModelViewSet):
    queryset = Plano.objects.all()
    serializer_class = PlanoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
