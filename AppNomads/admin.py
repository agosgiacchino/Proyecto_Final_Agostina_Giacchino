from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(Curso)

admin.site.register(Usuario)

admin.site.register(Nomade)

admin.site.register(Viajes)

admin.site.register(Avatar)
