from django.shortcuts import render
from django.http import JsonResponse
from Tarea1.models import Eventos

def listar_eventos(request):
    eventos = Eventos.objects.all()
    data = [{"titulo": p.titulo} for p in eventos]
    return JsonResponse(data, safe=False)


def eventos_segun_nombre(request):
    titulo = request.GET.get('titulo', "")
    evento = Eventos.objects.filter(titulo=titulo)
    lista = [{"titulo":event.titulo, "descripcion":event.descripcion, "fecha:hora":event.fecha_hora} for event in evento]
    return JsonResponse(lista, safe=False)
# Create your views here.
