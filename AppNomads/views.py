from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import *
from .forms import *

# Create your views here.
def inicio(request):
    try: 
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, 'inicio.html', {'url': avatar.imagen.url})
    except:
        return render(request, "inicio.html")
    
def AboutMe(request):
    return render(request, "aboutme.html")
    
#1er Círculo Inicio!!
@login_required   
def agregar_curso(request):
    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            curso = Curso(nombre=request.POST['nombre'], codigo=request.POST['codigo'],)
            curso.save()
            return render(request, "inicio.html", {"mensaje": "Muy bien agregaste tu curso para Digital Nomads :)"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = CursoFormulario()
        return render(request, "agregar_curso.html", {"mi_formulario": mi_formulario})

@login_required  
def lista_cursos(request):
    orden = request.GET.get('orden', None)
    cursos = Curso.objects.all()
    if orden == 'nombre':
        cursos = cursos.order_by('-codigo')
    return render(request, "ver_cursos.html", {"cursos": cursos})

@login_required
def eliminar_curso(request, id):
    if request.method == 'POST':
        curso = Curso.objects.get(id=id)
        curso.delete()
        curso = Curso.objects.all()
        return HttpResponseRedirect('/l-cursos')

@login_required    
def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            curso.nombre = data['nombre']
            curso.codigo = data['codigo']
            curso.save()
            return render(request, "inicio.html", {"mensaje": "Cambios realizados ;)"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = CursoFormulario(initial={
            "nombre": curso.nombre,
            "codigo": curso.codigo,
        })
        return render(request, "editar_cursos.html", {"mi_formulario": mi_formulario, "id": curso.id})

@login_required    
def agregar_nomade(request):
    mi_formulario = NomadesFormulario()
    if request.method == 'POST':
        mi_formulario = NomadesFormulario(request.POST)
        if mi_formulario.is_valid():
            mi_formulario.save()
            return HttpResponseRedirect('/l-nomades')
    return render(request, 'agregar_nomade.html', {'mi_formulario': mi_formulario})

@login_required
def lista_nomades(request):
    nomades = Nomade.objects.all()
    return render(request, 'lista_nomades.html', {'nomades': nomades})

@login_required
def eliminar_nomade(request, id):
    if request.method == 'POST':
        nomade = Nomade.objects.get(id=id)
        nomade.delete()
        nomade = Nomade.objects.all()
        return HttpResponseRedirect('/l-nomades')

login_required    
def editar_nomade(request, id):
    nomade = Nomade.objects.get(id=id)
    if request.method == 'POST':
        mi_formulario = NomadesFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            nomade.nombre = data['nombre']
            nomade.apellido = data['apellido']
            nomade.email = data['email']
            nomade.profesion = data['profesion']
            nomade.save()
            return render(request, "inicio.html", {"mensaje": "Cambios realizados ;)"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = NomadesFormulario(initial={
            "nombre": nomade.nombre,
            "apellido": nomade.apellido,
            "email": nomade.email,
        })
        return render(request, "editar_nomade.html", {"mi_formulario": mi_formulario, "id": nomade.id})
#1er Círculo Fin!!


#3er Círculo Inicio!!
@login_required
def lista_viajes(request):
    viajes = Viajes.objects.all()
    return render(request, 'viajes.html', {'viajes': viajes})

@login_required
def crear_viaje(request):
    if request.method == 'POST':
        form = ViajesFormulario(request.POST)
        if form.is_valid():
            viaje = form.save(commit=False)
            viaje.save()
            return HttpResponseRedirect('/foro')
    else:
        form = ViajesFormulario()
    return render(request, 'crear_viaje.html', {'form': form})

#3er Círculo Final

#El 4to Círculo está en AppMensajes