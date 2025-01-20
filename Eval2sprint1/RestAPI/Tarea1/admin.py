from django.contrib import admin
from .models import Usuarios, Eventos, Reservas, Comentarios

admin.site.register(Usuarios)
admin.site.register(Eventos)
admin.site.register(Reservas)
admin.site.register(Comentarios)


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'organizador', 'fecha_hora', 'capacidad_maxima')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('organizador',)

admin.site.register(Eventos, EventoAdmin)


# Register your models here.
