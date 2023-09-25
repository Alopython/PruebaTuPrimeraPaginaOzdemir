from django.shortcuts import render

from . import models


# Create your views here.

def index(request):
    clientes = models.Cliente.objects.all()    
    return render(request, "cliente/index.html",{"clientes":clientes})



