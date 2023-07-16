from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):

    nombre=models.CharField(max_length=40)
    codigo =models.IntegerField()
    def __str__(self):
        return f"nombre: {self.nombre} - codigo: {self.codigo}"


class Usuario(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    def __str__(self):
        return f"nombre: {self.nombre} - codigo: {self.codigo} - email: {self.email}"

class Nomade(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

class Viajes(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeViaje = models.DateField()  
    destino = models.BooleanField()
    def __str__(self):
        return f"{self.titulo}"

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #SubCarpeta de avatares
    imagen = models.ImageField(upload_to='avatares', null = True, blank = True)
