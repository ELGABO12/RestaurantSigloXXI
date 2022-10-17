from django.contrib import admin
from .models import Autor, Libro, Mesa, Receta, Bodega

# Register your models here.

admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Mesa)
admin.site.register(Receta)
admin.site.register(Bodega)