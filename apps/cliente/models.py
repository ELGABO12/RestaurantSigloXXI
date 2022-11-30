from unittest.util import _MAX_LENGTH
from django.db import models
from apps.mantenedor.models import Mesa, Receta

# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

class Reserva(models.Model):
    cod_reserva = models.AutoField(primary_key = True)
    email_cliente = models.EmailField(max_length = 255, blank = False, null = True)
    nombre_cliente = models.CharField(max_length = 200, blank = False, null = False)
    apellido_cliente = models.CharField(max_length = 200, blank = False, null = False)
    telefono_cliente = models.CharField(max_length = 12, blank = False, null = False)
    fecha_reserva = models.DateField('Fecha de la reserva', blank = True, null = True)
    hora_choice = {
        ('13:00', '13:00'), ('13:15', '13:15'), ('13:30', '13:30'), ('13:45', '13:45'),
        ('14:00', '14:00'), ('14:15', '14:15'), ('14:30', '14:30'), ('14:45', '14:45'),
        ('15:00', '15:00'), ('15:15', '15:15'), ('15:30', '15:30'), ('15:45', '15:45'),
        ('16:00', '16:00'), ('16:15', '16:15'), ('16:30', '16:30'), ('16:45', '16:45'),
    }
    hora_reserva = models.CharField('Hora de la reserva', max_length = 5, blank = True, null = True, choices=hora_choice)
    numero_mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL, null=True, blank=False)
    
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['cod_reserva']
        
    def __str__(self):
        return f'{self.nombre_cliente} {self.apellido_cliente}'


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------


class OrdenCompra(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_cliente = models.CharField('Nombre', max_length = 50, blank = False, null = True)
    apellido_cliente = models.CharField('Apellido', max_length = 50, blank = False, null = True)
    email_cliente = models.EmailField(max_length = 255, blank = False, null = True)
    mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL, null=True)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    ha_pagado = models.BooleanField(default=True)
    estado = models.BooleanField(default=False)
    entregado = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'OrdenCompra'
        verbose_name_plural = 'OrdenCompras'
        ordering = ('-fecha_orden',)
        
    def __str__(self):
        return 'Orden de Compra {}'.format(self.id)
    
    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------


class OrdenItem(models.Model):
    orden = models.ForeignKey(OrdenCompra, on_delete=models.SET_NULL,related_name='items', null = True)
    receta = models.ForeignKey(Receta, on_delete=models.SET_NULL, related_name='orden_items', null = True)
    precio_receta = models.FloatField('Precio de la receta', max_length=10)
    cantidad = models.PositiveIntegerField('Cantidad', default=1, null = False)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.precio_receta * self.cantidad
