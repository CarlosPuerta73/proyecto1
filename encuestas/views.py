from django.http import HttpResponse, request
from django.shortcuts import render, redirect

from utils import limpiar_texto
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, QueryDict
import json
from .models import Musician, Profesor, User

# Create your views here.

#def index(request):
#    return render (request, "code.html",{}) 

def get(request):
    hola = " m a l o"
    #texto = limpiar_texto(hola)
    return render(request,"codeejemplo.html",{"text":limpiar_texto(hola)})
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
        print("Usuario y contraseña recibidos:", usuario_input, password_input)
        #user = authenticate(request, username=usuario_input, password=password_input) 
        user = User.objects.filter(username=usuario_input, password=password_input).first()
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'code.html', {'error': '!!!..Usuario o contraseña incorrectos'})
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




@csrf_exempt 
def musico_view(request):
    print("-.--->", request.method)
    if request.method == "POST":
        print("Músico......", request.POST)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        instrument = request.POST.get("instrument")

        print(first_name, last_name, instrument)
        musico = Musician.objects.create(first_name=first_name, last_name=last_name, instrument=instrument)
        print("Músico creado:", musico)

        return JsonResponse({"status": "ok", "musico_name": musico.first_name})

    if request.method == "GET":
            print(request.GET)
            musico = Musician.objects.filter(first_name=request.GET.get("first_name"))
            print(musico)
            data = []
            for p in musico:
                data.append({"first_name": p.first_name, "last_name": p.last_name, "instrument": p.instrument})
            return JsonResponse({"status": "ok", "message": data})
    
    if request.method == "PUT":
        put_data = QueryDict(request.body)
        first_name = put_data.get("first_name")
        last_name = put_data.get("last_name")
        instrument = put_data.get("instrument")
        print("paso al put", first_name, last_name, instrument)
        # Aquí podrías manejar la actualización de un músico
        musico = Musician.objects.filter(first_name=first_name).first()
        print("---", musico)
        if musico:
            musico.last_name = last_name
            musico.instrument = instrument
            musico.save()
            return JsonResponse({"status": "ok", "message": "Músico actualizado"})
        else:
            return JsonResponse(
                {"status": "error", "message": "Músico   no encontrado"}
            )

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')

def registrar_usuario_view(request):
    return render(request, 'registrar_usuario.html')


@csrf_exempt 
def form_registrar_usuario_view(request):
    print(request.POST);
    print("-.--->", request.method)

    if request.method == "POST":
        print("Usuario......", request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        user = User.objects.filter(username=username).first()
        print("---", user)
        if user:
            return JsonResponse({"status": "ok", "message": "Usuario ya esta registrado"})

        print(username, password, password2)
        user = User.objects.create(username=username, password=password)
        print("Usuario creado:", user)
        user.save()

        #return JsonResponse({"status": "ok", "user_name": user.username })
        return redirect('login')

    if request.method == "GET":
            print(request.GET)
            user = User.objects.filter(username=request.GET.get("username"))
            print(user)
            data = []
            for p in user:
                data.append({"username": p.username, "password": p.password, "password2": p.password2})
            return JsonResponse({"status": "ok", "message": data})
    
    if request.method == "PUT":
        put_data = QueryDict(request.body)
        username = put_data.get("username")
        password = put_data.get("password")
        password2 = put_data.get("password2")
        print("paso al put", username, password, password2)
        # Aquí podrías manejar la actualización de un usuario
        user = User.objects.filter(username=username).first()
        print("---", user)
        if user:
            user.password = password
            user.password2 = password2
            user.save()
            return JsonResponse({"status": "ok", "message": "Usuario actualizado"})
        else:
            return JsonResponse(
                {"status": "error", "message": "Usuario   no encontrado"}
            )
