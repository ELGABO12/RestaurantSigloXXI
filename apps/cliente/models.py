from unittest.util import _MAX_LENGTH
from django.db import models
from apps.libro.models import Mesa

# Create your models here.


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
    numero_mesa = models.ManyToManyField(Mesa)
    
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['cod_reserva']
        
    def __str__(self):
        return self.nombre_cliente