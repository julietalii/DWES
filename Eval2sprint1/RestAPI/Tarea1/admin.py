from django.contrib import admin
from .models import Usuarios, Eventos, Reservas, Comentarios

admin.site.register(Usuarios)
admin.site.register(Eventos)
admin.site.register(Reservas)
admin.site.register(Comentarios)


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_hora', 'capacidad')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('fecha_hora')




# Register your models here.
