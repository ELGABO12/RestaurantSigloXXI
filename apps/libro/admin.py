from django.contrib import admin
from .models import Autor, Libro, Mesa, Receta

# Register your models here.

admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Mesa)
admin.site.register(Receta)