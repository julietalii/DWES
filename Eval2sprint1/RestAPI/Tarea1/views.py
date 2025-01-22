from django.shortcuts import render
from django.http import JsonResponse
from Tarea1.models import Eventos

def listar_eventos(request):
    eventos = Eventos.objects.all()
    data = [{"titulo": p.titulo} for p in eventos]
    return JsonResponse(data, safe=False)
# Create your views here.
