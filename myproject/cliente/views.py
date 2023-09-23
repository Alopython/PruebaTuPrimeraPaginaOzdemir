from django.shortcuts import render


# Create your views here.

def index(request):
    contexto = {"nombre": "Ingeniero"}
    return render(request, "cliente/index.html",contexto)