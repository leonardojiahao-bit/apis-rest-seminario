from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, DespesaViewSet, ReceitaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'despesas', DespesaViewSet)
router.register(r'receitas', ReceitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
