
import random

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader


from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required


from indice.forms import NuestraCreacionUser, NuestraEdicionUser

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


def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            
            if user is not None:
                django_login(request, user)
                
                return render(request, 'indice/index.html', {'msj': 'Te logeaste!'})
            else:
                return render(request,
                              'indice/login.html', {
                              'form': form,
                              'msj': 'No se auntentico'})
        else:
            form = AuthenticationForm()
            return render(request, 
                          'indice/login.html', 
                          {'form': form, 
                           'msj': 'Datos con formato incorrecto'
                           }
                          )
            
    # django_login, authenticate
    
    form = AuthenticationForm()
    return render(request, 'indice/login.html', {'form': form, 'msj': ''})


def registrar(request):
    
    if request.method == 'POST':
        form = NuestraCreacionUser(request.POST)
    
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'indice/index.html', {'msj': f'Se creo el user {username}'})
        else:
            return render(request, 'indice/registrar.html', {'form': form, 'msj': 'Datos incorrectos'})
            
        
    form = NuestraCreacionUser()
    
    return render(request, 'indice/registrar.html', {'form': form, 'msj': ''})

@login_required
def editar(request):
    
    request.user

    if request.method == 'POST':
        form = NuestraEdicionUser(request.POST)
    
        if form.is_valid():

            data = form.cleaned_data

            request.user.username = data.get('username')
            request.user.email = data.get('email')
            request.user.first_name = data.get('first_name', '')
            request.user.last_name = data.get('last_name')
            if data.get('password1') == data.get('password2') and len(data.get('password1')) > 8:
                request.user.set_password(data.get('password1'))
            else:
                msj = 'No se modifico el password.'
            
            request.user.save()

            return render(request, 'indice/index.html', {'msj': f'Se edito el user {request.user.username}'})
        else:
            return render(request, 'indice/editar_user.html', {'form': form, 'msj': 'Datos incorrectos'})
            
        
    form = NuestraEdicionUser(
        initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'username': request.user.username,
        }
    )
    # return render(request, 'indice/index.html', {'msj': ''})
    
    return render(request, 'indice/editar_user.html', {'form': form, 'msj': ''})
    