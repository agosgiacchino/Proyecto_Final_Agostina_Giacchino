from django.contrib import admin
from django.urls import path 
from .views import *







urlpatterns = [
   
    path('', inicio, name="Inicio"), #esta era nuestra primer view
    path('ag-curso', agregar_curso, name="AgregarCurso"),
    path('l-cursos', lista_cursos, name="ListaCursos"),
    path('el-cursos/<int:id>', eliminar_curso, name="EliminarCurso"),
    path('ed-curso/<int:id>', editar_curso, name="EditarCurso"),
    path('ag-nomade', agregar_nomade, name='AgregarNomade'),
    path('l-nomades', lista_nomades, name='ListaNomades'),
    path('el-nomades/<int:id>', eliminar_nomade, name="EliminarNomade"),
    path('ed-nomades/<int:id>', editar_nomade, name="EditarNomade"),
    path('about-me', AboutMe, name="AboutMe"),
    path('foro', lista_viajes, name='Foro'),
]