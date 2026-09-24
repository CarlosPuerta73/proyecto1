from django.http import HttpResponse
from django.shortcuts import render, redirect

from utils import limpiar_texto
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required 

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