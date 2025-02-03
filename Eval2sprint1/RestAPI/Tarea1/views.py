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


#PUT/PATCH:
# Actualizar un evento (solo organizadores)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Tarea1.models import Eventos, Usuarios
import json


@csrf_exempt
def actualizar_evento(request):
    if request.method in ["PUT", "PATCH"]:
        try:
            info = json.loads(request.body)


            username = info.get("usuario", "")
            titulo_evento = info.get("titulo", "")


            usuario = Usuarios.objects.filter(username=username).first()
            if not usuario:
                return JsonResponse({"error": "Usuario no encontrado."}, status=404)


            evento = Eventos.objects.filter(titulo=titulo_evento).first()
            if not evento:
                return JsonResponse({"error": "Evento no encontrado."}, status=404)

            if usuario.rol != "organizador":
                return JsonResponse({"error": "No tienes permisos para actualizar eventos."}, status=403)


            if hasattr(evento, 'usuario') and usuario != evento.usuario:
                return JsonResponse({"error": "Solo el organizador del evento puede actualizarlo."}, status=403)


            evento.descripcion = info.get("descripcion", evento.descripcion)
            evento.fecha_hora = info.get("fecha_hora", evento.fecha_hora)
            evento.capacidad = info.get("capacidad", evento.capacidad)
            evento.url = info.get("url", evento.url)
            evento.save()

            return JsonResponse({"mensaje": "Evento actualizado correctamente."})

        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Error inesperado: {str(e)}"}, status=500)

    return JsonResponse({"error": "Método no permitido."}, status=405)
#DELETE:
@csrf_exempt
def eliminar_evento(request):
    if request.method == "DELETE":
        try:
            info = json.loads(request.body)

            # Toma el username del usuario y el título del evento
            username = info.get("usuario", "")
            titulo_evento = info.get("titulo", "")

            # Verifica que el usuario existe
            usuario = Usuarios.objects.filter(username=username).first()
            if not usuario:
                return JsonResponse({"error": "Usuario no encontrado."}, status=404)

            # Verifica que el evento existe antes de eliminarlo
            evento = Eventos.objects.filter(titulo=titulo_evento).first()
            if not evento:
                return JsonResponse({"error": "Evento no encontrado."}, status=404)

            # Verifica si el usuario es organizador
            if usuario.rol != "organizador":
                return JsonResponse({"error": "No tienes permisos para eliminar eventos."}, status=403)

            # Si el modelo tiene "usuario", verifica que el usuario creó el evento
            if hasattr(evento, 'usuario') and usuario != evento.usuario:
                return JsonResponse({"error": "Solo el organizador del evento puede eliminarlo."}, status=403)

            # Eliminar el evento
            evento.delete()

            return JsonResponse({"mensaje": "Evento eliminado correctamente."})

        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Error inesperado: {str(e)}"}, status=500)

    return JsonResponse({"error": "Método no permitido."}, status=405)


#punto 2: reservas
#get:

@csrf_exempt
def listar_reservas_usuario(request):
    if request.method == "GET":
        try:
            info = json.loads(request.body)
            username = info.get("usuario", "")

            usuario = Usuarios.objects.filter(username=username).first()
            if not usuario:
                return JsonResponse({"error": "Usuario no encontrado."}, status=404)

            reservas = Reservas.objects.filter(id_usuario=usuario)
            reservas_lista = [{"evento": r.id_evento.titulo, "entradas": r.entradas, "estado": r.estado} for r in reservas]

            return JsonResponse({"reservas": reservas_lista}, safe=False)

        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Error inesperado: {str(e)}"}, status=500)

    return JsonResponse({"error": "Método no permitido."}, status=405)


#POST:
@csrf_exempt
def crear_reserva(request):
    if request.method == "POST":
        try:
            info = json.loads(request.body)
            username = info.get("usuario", "")
            titulo_evento = info.get("evento", "")
            entradas = int(info.get("entradas", 1))

            usuario = Usuarios.objects.filter(username=username).first()
            if not usuario:
                return JsonResponse({"error": "Usuario no encontrado."}, status=404)

            evento = Eventos.objects.filter(titulo=titulo_evento).first()
            if not evento:
                return JsonResponse({"error": "Evento no encontrado."}, status=404)

            # Verificar disponibilidad de entradas
            reservas_actuales = Reservas.objects.filter(id_evento=evento).count()
            if reservas_actuales + entradas > evento.capacidad:
                return JsonResponse({"error": "No hay suficientes espacios disponibles."}, status=400)

            # Crear la reserva
            reserva = Reservas.objects.create(id_usuario=usuario, id_evento=evento, entradas=entradas)
            return JsonResponse({"mensaje": "Reserva creada correctamente."})

        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Error inesperado: {str(e)}"}, status=500)

    return JsonResponse({"error": "Método no permitido."}, status=405)

#PUT/PATCH:
@csrf_exempt
def actualizar_reserva(request):
    if request.method in ["PUT", "PATCH"]:
        try:
            info = json.loads(request.body)
            username = info.get("usuario", "")
            titulo_evento = info.get("evento", "")
            nuevo_estado = info.get("estado", "")

            usuario = Usuarios.objects.filter(username=username).first()
            if not usuario:
                return JsonResponse({"error": "Usuario no encontrado."}, status=404)

            if usuario.rol != "organizador":
                return JsonResponse({"error": "No tienes permisos para actualizar reservas."}, status=403)

            reserva = Reservas.objects.filter(id_evento__titulo=titulo_evento).first()
            if not reserva:
                return JsonResponse({"error": "Reserva no encontrada."}, status=404)

            reserva.estado = nuevo_estado
            reserva.save()

            return JsonResponse({"mensaje": "Estado de la reserva actualizado correctamente."})

        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Error inesperado: {str(e)}"}, status=500)

    return JsonResponse({"error": "Método no permitido."}, status=405)
# delete:
@csrf_exempt
def cancelar_reserva(request):
    if request.method == "DELETE":
        try:
            info = json.loads(request.body)
            username = info.get("usuario", "")
            titulo_evento = info.get("evento", "")

            usuario = Usuarios.objects.filter(username=username).first()
            if not usuario:
                return JsonResponse({"error": "Usuario no encontrado."}, status=404)

            reserva = Reservas.objects.filter(id_evento__titulo=titulo_evento, id_usuario=usuario).first()
            if not reserva:
                return JsonResponse({"error": "Reserva no encontrada."}, status=404)

            reserva.delete()

            return JsonResponse({"mensaje": "Reserva cancelada correctamente."})

        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Error inesperado: {str(e)}"}, status=500)

    return JsonResponse({"error": "Método no permitido."}, status=405)
#
# Create your views here.
