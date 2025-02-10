"""
URL configuration for RestAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Tarea1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar_eventos', views.listar_eventos),
    path('evento/', views.eventos_segun_nombre),
    path('crear_evento', views.crear_evento),
    path('eventospagina', views.eventos_por_paginas),
    path('actualizar_evento', views.actualizar_evento),
    path('eliminar_evento', views.eliminar_evento),

    path('listar_reservas_usuario/', views.listar_reservas_usuario),
    path('crear_reserva', views.crear_reserva),
    path('actualizar_reserva', views.actualizar_reserva),
    path('cancelar_reserva', views.cancelar_reserva),

    path('listar_comentarios', views.listar_comentarios),
    path('crear_comentario', views.crear_comentario),

    path('registrar_usuario', views.registrar_usuario),
    path('login_usuario', views.login_usuario),

]
