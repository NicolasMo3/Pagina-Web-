from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    # Muestra estos campos en la lista
    list_display = ('nombre', 'email', 'telefono', 'producto', 'fecha_in', 'fecha_sal')
    # Permite buscar por estos campos
    search_fields = ('nombre', 'email')
    # Agrega un filtro para los campos de fecha
    list_filter = ('fecha_in', 'fecha_sal', 'sucursal', 'estado')

# Registra el modelo con su clase personalizada de administración
admin.site.register(Cliente, ClienteAdmin)
