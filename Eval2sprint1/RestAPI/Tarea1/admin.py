from django.contrib import admin
from .models import Usuarios, Eventos, Reservas, Comentarios


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_hora', 'capacidad')
    search_fields = ('titulo',)
    list_filter = ('fecha_hora',)

admin.site.register(Usuarios)
admin.site.register(Eventos, EventoAdmin)
admin.site.register(Reservas)
admin.site.register(Comentarios)


# Register your models here.
