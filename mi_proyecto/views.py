from django.http import HttpResponse

# Create your views here.

def page(request):
    return HttpResponse("<h1>!Hola Esta es la pagina principal de Encuesta. </h1>")