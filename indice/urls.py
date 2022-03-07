
from django.contrib import admin
from django.urls import path
from .views import inicio, otra_vista, numero_random, numero_del_usuario, calcular_nacimiento, mi_plantilla

urlpatterns = [
    path('inicio/', inicio),
    path('', otra_vista),
    path('numero-random/', numero_random),
    path('dame-numero/<int:numero>', numero_del_usuario),
    path('calcular-nacimiento/<int:edad>', calcular_nacimiento),
    path('mi-plantilla/', mi_plantilla)
]