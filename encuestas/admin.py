from django.contrib import admin
from .models import Album, PerfilEstudiante, Profesor, Curso, Estudiante, Musician

admin.site.register(PerfilEstudiante)
admin.site.register(Profesor)   
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Musician)
admin.site.register(Album)
# Register your models here.
