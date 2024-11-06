from django.contrib import admin
from .models import Cliente

admin.site.register(Cliente)

class ClienteAdmin(admin.ModelAdmin):
    # Muestra estos campos en la lista
    list_display = ('nombre', 'email', 'telefono')
    # Permite buscar por estos campos
    search_fields = ('nombre', 'email')
    # Agrega un filtro por fecha de contacto
    list_filter = ('fecha_contacto',)