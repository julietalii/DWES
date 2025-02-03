from django.shortcuts import render
from django.http import JsonResponse
from Tarea1.models import Eventos, Usuarios, Reservas, Comentarios
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import json

def listar_eventos(request):
    eventos = Eventos.objects.all()
    data = [{"titulo": e.titulo, "descripcion": e.descripcion, "fecha_hora": e.fecha_hora, "capacidad": e.capacidad, "url": e.url} for e in eventos]
    return JsonResponse(data, safe=False)


# Buscar evento por título
def eventos_segun_nombre(request):
    titulo = request.GET.get('titulo', "")
    evento = Eventos.objects.filter(titulo__icontains=titulo)
    lista = [{"titulo": e.titulo, "descripcion": e.descripcion,
              "fecha_hora": e.fecha_hora, "capacidad": e.capacidad, "url": e.url} for e in evento]
    return JsonResponse(lista, safe=False)
# eg

# Listar eventos con paginación
def eventos_por_paginas(request):
    titulo = request.GET.get("titulo", "")
    orden = request.GET.get("orden", "titulo")
    limite = int(request.GET.get("limite", 5))
    pagina = int(request.GET.get("pagina", 1))
    evento = Eventos.objects.filter(titulo__icontains=titulo).order_by(orden)

    paginator = Paginator(evento, limite)
    try:
        evento_pagina = paginator.page(pagina)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

    lista = {
        "count": paginator.count,
        "total_paginas": paginator.num_pages,
        "pagina_actual": pagina,
        "siguiente": pagina + 1 if evento_pagina.has_next() else None,
        "anterior": pagina - 1 if evento_pagina.has_previous() else None,
        "resultado": [
            {"titulo": e.titulo, "descripcion": e.descripcion, "fecha_hora": e.fecha_hora, "capacidad": e.capacidad,
             "url": e.url} for e in evento_pagina]
    }
    return JsonResponse(lista, safe=False)
# eg


#POST:
# Crear un evento
@csrf_exempt
def crear_evento(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            usuario = Usuarios.objects.get(username=data["usuario"])
            if usuario.rol != "organizador":
                return JsonResponse({"error": "No tienes permisos para crear eventos."}, status=403)

            evento = Eventos.objects.create(
                titulo=data["titulo"],
                descripcion=data["descripcion"],
                fecha_hora=data["fecha_hora"],
                capacidad=data["capacidad"],
                url=data["url"]
            )
            return JsonResponse({"mensaje": "Evento creado correctamente.", "titulo": evento.titulo})
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Usuarios.DoesNotExist:
            return JsonResponse({"error": "Usuario no encontrado."}, status=404)
        except KeyError as e:
            return JsonResponse({"error": f"Falta el campo {str(e)}"}, status=400)
    return JsonResponse({"error": "Método no permitido."}, status=405)
#adaptando 29-01-2025


# Create your views here.
