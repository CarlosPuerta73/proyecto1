from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>!Hola Esta es la pagina principal de Encuesta. </h1>")