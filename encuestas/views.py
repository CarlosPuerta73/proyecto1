from django.http import HttpResponse
from django.shortcuts import render, redirect

from utils import limpiar_texto
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, QueryDict
import json
from .models import Profesor

# Create your views here.

#def index(request):
#    return render (request, "code.html",{}) 

def get(request):
    hola = " m a l o"
    #texto = limpiar_texto(hola)
    return render(request,"code.html",{"text":limpiar_texto(hola)})
#def index(request):
#    return HttpResponse("<h1>!Hola Esta es la pagina principal de Encuesta. </h1>")

@login_required
def home_view(request):
    contexto =  {'usuario': request.user }
    return render(request, 'home.html', contexto)

def login_view(request):
    if request.method == "POST":
        usuario_input = request.POST.get("username")
        password_input = request.POST.get("password")

        user = authenticate(request, username=usuario_input, password = password_input)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'code.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, "code.html")

@csrf_exempt 
def profesor_view(request):
    print("-.--->", request.method)
    if request.method == "POST":
        print("Profesor......", request.POST)
        nombre = request.POST.get("nombre")
        especialidad = request.POST.get("especialidad")

        print(nombre, especialidad)
        profesor = Profesor.objects.create(nombre=nombre, especialidad=especialidad)
        print("Profesor creado:", profesor)

        return JsonResponse({"status": "ok", "profesor_name": profesor.nombre})

    if request.method == "GET":
            print(request.GET)
            profesor = Profesor.objects.filter(nombre=request.GET.get("nombre"))
            print(profesor)
            data = []
            for p in profesor:
                data.append({"nombre": p.nombre, "especialidad": p.especialidad})
            return JsonResponse({"status": "ok", "message": data})
    
    if request.method == "PUT":
        put_data = QueryDict(request.body)
        nombre = put_data.get("nombre")
        especialidad = put_data.get("especialidad")
        print("paso al put", nombre, especialidad)
        # Aquí podrías manejar la actualización de un profesor
        profesor = Profesor.objects.filter(nombre=nombre).first()
        print("---", profesor)
        if profesor:
            profesor.especialidad = especialidad
            profesor.save()
            return JsonResponse({"status": "ok", "message": "Profesor actualizado"})
        else:
            return JsonResponse(
                {"status": "error", "message": "Profesor no encontrado"}
            )
