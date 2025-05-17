from django.contrib import admin
from .models import Cliente, PerfilUsuario

class ClienteAdmin(admin.ModelAdmin):
    # Muestra estos campos en la lista
    list_display = ('nombre', 'email', 'telefono', 'producto', 'fecha_in')
    # Permite buscar por estos campos
    search_fields = ('nombre', 'email')
    # Agrega un filtro para los campos de fecha
    list_filter = ('fecha_in', 'sucursal', 'estado')

# Registra el modelo con su clase personalizada de administración
admin.site.register(Cliente, ClienteAdmin)

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_encuesta_script')  # Muestra el usuario y su encuesta

    def get_encuesta_script(self, obj):
        return obj.encuesta_script if obj.encuesta_script else "No asignado"

    get_encuesta_script.short_description = "Encuesta Script"