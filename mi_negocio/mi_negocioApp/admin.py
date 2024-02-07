from django.contrib import admin
from mi_negocioApp.models import *




class Producto_admin(admin.ModelAdmin):
    list_display = ("precio", "tipo_producto")
    search_fields = ("tipo_producto",)
    list_filter = ("precio",)

class Cliente_admin(admin.ModelAdmin):
    list_display = ("carnet_id", "numero_telefono", "nombre",  "direccion",)
    search_fields = ("carnet_id",  "numero_telefono", "nombre", )
    list_filter = ("carnet_id",)


admin.site.register(Producto, Producto_admin)
admin.site.register(Cliente, Cliente_admin)
