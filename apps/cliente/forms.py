from socket import fromshare
from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['email_cliente', 'nombre_cliente', 'apellido_cliente', 'telefono_cliente', 
                  'fecha_reserva', 'hora_reserva', 'numero_mesa']
        labels = {
            'email_cliente': 'Correo electrónico del cliente',
            'nombre_cliente': 'Nombre del cliente',
            'apellido_cliente': 'Apellido del cliente',
            'telefono_cliente': 'Número de teléfono del cliente',
            'fecha_reserva': 'Día de la reserva',
            'hora_reserva': 'Hora de la reserva',
            'numero_mesa': 'Elija la mesa que desea reservar',
        }
        widgets = {
            'email_cliente': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese correo del cliente'
                }
            ),
            'nombre_cliente': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese nombre del cliente'
                }
            ),
            'apellido_cliente': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese apellido del cliente'
                }
            ),
            'telefono_cliente': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese número de teléfono del cliente'
                }
            ),
            'fecha_reserva': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'hora_reserva': forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'numero_mesa': forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
        }