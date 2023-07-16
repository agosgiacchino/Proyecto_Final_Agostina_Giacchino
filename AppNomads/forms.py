from django import forms
from .models import *

class CursoFormulario(forms.Form):

    #Especificar los campos
    curso = forms.CharField()
    codigo = forms.IntegerField()


class NomadesFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class ViajesFormulario(forms.Form):
        nombre = forms.CharField()
        fecha_de_viaje = forms.CharField()
        destino = forms.CharField()