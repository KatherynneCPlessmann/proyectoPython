from django.contrib import admin

from peach.models import *

class TipoArticuloAdmin(admin.ModelAdmin):
    list_display = ["nombre"]

class TipoServicioAdmin(admin.ModelAdmin):
    list_display = ["nombre"]

class EstadoAdmin(admin.ModelAdmin):
    list_display = ["estado"]

class EncuestaAdmin(admin.ModelAdmin):
    list_display = ["ocupacion", "experiencia", "estado"]
    ordering = ["experiencia"]
    search_fields = ["ocupacion"]

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "Tipo"]
    ordering = ["precio"]
    search_fields = ["nombre"]

class ServicioAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion", "costo", "Tipo"]
    ordering = ["costo"]
    search_fields = ["nombre"]

class CompraAdmin(admin.ModelAdmin):
    list_display = ["numero","fecha"]
    list_filter = ["fecha"]
    date_hierarchy = "fecha"

class VentaAdmin(admin.ModelAdmin):
    list_display = ["numero","fecha", "costoAdicional", "cliente"]
    list_filter = ["fecha"]
    date_hierarchy = "fecha"

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ["nombres", "empresa", "telefono", "correo", "direccion"]
    search_fields = ["empresa"]

class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nombres", "empresa", "telefono", "correo", "direccion", "referencia"]
    search_fields = ["empresa"]

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ["nombre","fecha", "descripcion"]
    list_filter = ["fecha"]
    date_hierarchy = "fecha"

class ContactoAdmin(admin.ModelAdmin):
    list_display = ["nombres", "empresa", "telefono", "correo", "interes"]
    search_fields = ["empresa"]


admin.site.register(TipoArticulo, TipoArticuloAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(TipoServicio, TipoServicioAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Contacto, ContactoAdmin)