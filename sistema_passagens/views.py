from rest_framework import viewsets
from .models import Aeroporto, Voo, Passagem
from .serializers import AeroportoSerializer, VooSerializer, PassagemSerializer


class AeroportoViewSet(viewsets.ModelViewSet):
    queryset = Aeroporto.objects.all()
    serializer_class = AeroportoSerializer


class VooViewSet(viewsets.ModelViewSet):
    queryset = Voo.objects.all()
    serializer_class = VooSerializer


class PassagemViewSet(viewsets.ModelViewSet):
    queryset = Passagem.objects.all()
    serializer_class = PassagemSerializer
