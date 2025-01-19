from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuarios(AbstractUser):
    rol=models.CharField(max_length=20)
    biografia=models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Eventos(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_hora = models.DateTimeField()
    capacidad = models.IntegerField()
    url = models.URLField()
    def __str__(self):
        return self.titulo

class Comentarios(models.Model):
    texto = models.TextField()
    id_evento = models.ForeignKey(Eventos, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.texto

class Reservas(models.Model):
    informacion = models.TextField()
    id_evento = models.ForeignKey(Eventos, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    entradas = models.IntegerField()
    estado = models.CharField(max_length=20)
    def __str__(self):
        return self.informacion
# Create your models here.

