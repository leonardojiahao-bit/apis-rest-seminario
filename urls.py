from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/financeiro/', include('sistema_financeiro.urls')),
    path('api/academia/', include('sistema_academia.urls')),
    path('api/clinica/', include('sistema_clinica.urls')),
    path('api/oficina/', include('sistema_oficina.urls')),
    path('api/passagens/', include('sistema_passagens.urls')),
    path('api/hospital/', include('sistema_hospital.urls')),
]
