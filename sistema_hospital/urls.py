from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EspecialidadeViewSet, MedicoViewSet, PacienteViewSet, AgendamentoConsultaViewSet

router = DefaultRouter()
router.register(r'especialidades', EspecialidadeViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'agendamentos', AgendamentoConsultaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
