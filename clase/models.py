from django.db import models

# Create your models here.

class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=20) 
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
# Dejar dos espacios entre cada clase para mantener orden del codigo
# Comentarios no pasa nada

class Profesor(models.Model):
    
    nombre = models.CharField(max_length=20) 
    apellido = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)
    email = models.EmailField()


class Entregable(models.Model):
    
    nombre = models.CharField(max_length=20) 
    fechaDeEntrega = models.DateTimeField()
    entregado = models.BooleanField()


class Curso(models.Model):
    
    nombre = models.CharField(max_length=20) 
    camada = models.IntegerField() 

    def __str__(self):
        return f'Curso: {self.nombre} - Camada: {self.camada}'
