from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AeroportoViewSet, VooViewSet, PassagemViewSet

router = DefaultRouter()
router.register(r'aeroportos', AeroportoViewSet)
router.register(r'voos', VooViewSet)
router.register(r'passagens', PassagemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
