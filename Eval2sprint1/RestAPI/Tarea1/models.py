from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuarios(AbstractUser):
    ROLES = [
        ('organizador', 'Organizador'),
        ('participante', 'Participante'),
    ]
    rol = models.CharField(max_length=20, choices=ROLES, default='participante')
    biografia = models.TextField()
    groups = models.ManyToManyField(Group, related_name='tarea1_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='tarea1_users_permissions', blank=True)

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
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    def __str__(self):
        return self.informacion

# Create your models here.

