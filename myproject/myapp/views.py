from django.shortcuts import render



# Create your views here.

def index(request):
    contexto = {"nombre": "Reliability & Maintenance"}
    return render(request, "myapp/index.html",contexto)