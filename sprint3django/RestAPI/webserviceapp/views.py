from django.http import HttpResponse, JsonResponse
from .models import Tlibros  
from django.shortcuts import render
#from django.views.decorators.csrf import csrf_exempt
import json

#from .models import Tlibros
#from .models import Tcomentarios

def pagina_de_prueba(request):
	return HttpResponse("<h1>Hola a todos</h1>");

def devolver_libros(request):
	lista = Tlibros.objects.all()
	respuesta_final=[]
	for fila_sql in lista:
		diccionario = {}
		diccionario['id'] = fila_sql.id
		diccionario['nombre'] = fila_sql.nombre
		diccionario['url_img'] = fila_sql.url_imagen
		diccionario['autor'] = fila_sql.autor
		diccionario['fecha_publicacion'] = fila_sql.fecha_publicacion
		respuesta_final.append(diccionario)
	return JsonResponse(respuesta_final, safe=False)
