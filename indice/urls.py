
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name='inicio'),
    path('otra-vista', otra_vista, name='otra_vista'),
    path('numero-random/', numero_random, name='numer_random'),
    path('dame-numero/<int:numero>', numero_del_usuario,name='dame_numero'),
    path('calcular-nacimiento/<int:edad>', calcular_nacimiento, name='calcular_nacimiento'),
    path('mi-plantilla/', mi_plantilla, name='mi_plantilla'),
    path('login/', login, name='login'),
    path('registrar/', registrar, name='registrar'),
    path('editar/', editar, name='editar'),
    path('logout/', LogoutView.as_view(template_name='indice/logout.html'), name='logout'),
]