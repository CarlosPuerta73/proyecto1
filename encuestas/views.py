from django.shortcuts import render 
from django.http import HttpResponse
from utils import limpiar_texto
# Create your views here.

def index(request):
#    return render (request, "code.html",{}) 



#def get(request):
    hola = " m a l o"
    texto = limpiar_texto(hola)
    return HttpResponse(texto.encode("utf-8"), content_type="text/plain")
#def index(request):
#    return HttpResponse("<h1>!Hola Esta es la pagina principal de Encuesta. </h1>")

