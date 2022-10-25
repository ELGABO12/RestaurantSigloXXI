from django.contrib import admin
from .models import Producto, Proveedor, Mesa, Receta, Bodega

# Register your models here.

admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Mesa)
admin.site.register(Receta)
admin.site.register(Bodega)