from django.contrib import admin
from .models import Reserva, Boleta, OrdenCompra, OrdenItem

# Register your models here.

admin.site.register(Reserva)
admin.site.register(Boleta)
admin.site.register(OrdenCompra)
admin.site.register(OrdenItem)