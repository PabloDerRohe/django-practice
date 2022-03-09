
from django.contrib import admin
from django.urls import path
from .views import inicio, otra_vista, numero_random, numero_del_usuario, calcular_nacimiento, mi_plantilla

urlpatterns = [
    path('', inicio, name='inicio'),
    path('otra-vista', otra_vista, name='otra_vista'),
    path('numero-random/', numero_random, name='numer_random'),
    path('dame-numero/<int:numero>', numero_del_usuario,name='dame_numero'),
    path('calcular-nacimiento/<int:edad>', calcular_nacimiento, name='calcular_nacimiento'),
    path('mi-plantilla/', mi_plantilla, name='mi_plantilla')
]