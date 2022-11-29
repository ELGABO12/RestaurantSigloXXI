from django.contrib import admin
from .models import Reserva, OrdenCompra, OrdenItem

# Register your models here.

admin.site.register(Reserva)
admin.site.register(OrdenCompra)
admin.site.register(OrdenItem)