
from django.http import HttpResponse
import random
from django.shortcuts import render

from django.template import loader

# Vistas de prueba

def inicio(request):
    
    return render(request, "indice/index.html", {})

def otra_vista(request):
    return HttpResponse('''
                        <h1>Este es un titulo en h1</h1>
                        ''')
    
def numero_random(request):
    numero = random.randrange(15, 180)
    texto = f'<h1>Este es tu numero random: {numero}</h1>'
    return HttpResponse(texto)

def numero_del_usuario(request, numero):
    texto = f'<h1>Este es tu numero: {numero}</h1>'
    return HttpResponse(texto)

def calcular_nacimiento(request, edad):
    nacimiento = (2022 - int(edad))
    texto = f'<h1>Este es tu anio de nacimiento: {nacimiento}</h1>'
    return HttpResponse(texto)

# Vista mi_plantilla

def mi_plantilla(request):
    
    nombre = 'Raul'
    apellido = 'Atahualpa'
    
    lista = [3,1,2,45,1,2,3]
    
    diccionario_de_datos = {
        'nombre': nombre,
        'apellido': apellido, 
        'nombre_largo': len(nombre),
        'lista': lista
    }    
    
    #### Version vieja con open
    # plantilla = open('/home/pablo/projects_vm/coderpython_vm/miproyecto/miproyecto/plantillas/mi_plantilla.html',)
    # template = Template(plantilla.read())
    # plantilla.close()
    # context = Context(diccionario_de_datos)
    # plantilla_preparada = template.render(diccionario_de_datos)
    
    #### Version nueva con loader
    # Loader
    # template = loader.get_template('mi_plantilla.html')
    # # Render
    # plantilla_preparada = template.render(diccionario_de_datos)
    # # Response
    # return HttpResponse(plantilla_preparada)
    
    #### Version con render
    return render(request, 'indice/mi_plantilla.html', diccionario_de_datos)
    
    